import mysql.connector

conn = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'Yashr@7088',
    database = 'Relatify',
    port = 3306
)

cursor = conn.cursor()

def createFest(orgId: int, n: int):
    """
    Creates a new fest and its events.
    Logic:
    1. Prompt organizer for: FestName, City, StartDate, DescriptionFest
    2. Insert into Fests
    3. Get the FestId of the inserted record
    4. Loop n times to create events and insert into EventsInFest
    """
    try:
        fest_name = input("Enter Fest Name: ").strip()
        city = input("Enter City: ").strip()
        start_date = input("Enter Start Date (YYYY-MM-DD): ").strip()
        description = input("Enter Description: ").strip()

        insert_fest = """INSERT INTO Fests (FestName, City, StartDate, DescriptionFest)
                         VALUES (%s, %s, %s, %s)"""
        cursor.execute(insert_fest, (fest_name, city, start_date, description))
        conn.commit()

        fest_id = cursor.lastrowid
        print(f"Fest created successfully with FestId: {fest_id}")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS OrganizerFests (
                OrgId INT,
                FestId INT,
                Role VARCHAR(50),
                PRIMARY KEY (OrgId, FestId)
            )
        """)

        insert_orgfest = """INSERT INTO OrganizerFests (OrgId, FestId, Role)
                            VALUES (%s, %s, %s)"""
        cursor.execute(insert_orgfest, (orgId, fest_id, "Owner"))
        conn.commit()

        for i in range(n):
            print(f"\nEnter details for Event {i+1}:")
            event_name = input("Event Name: ").strip()
            event_description = input("DescriptionEvent: ").strip()
            event_date = input("Event Date (YYYY-MM-DD): ").strip()
            event_time = input("Event Time (HH:MM:SS): ").strip()

            insert_event = """INSERT INTO EventsInFest
                (FestId, EventName, DescriptionEvent, EventDate, EventTime)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_event, (fest_id, event_name, event_description, event_date, event_time))
            conn.commit()
            print(f"Event '{event_name}' added to FestId {fest_id}")

        print("All events added successfully.")

    except Exception as e:
        conn.rollback()
        print("Error creating fest:", e)

def viewFestDetails(orgId: int):
    """
    Displays all fests created by this organizer.
    Logic: use OrganizerFests mapping table to find fest ids,
           then return the matching rows from Fests.
    Returns a dict: {"status": "success", "fests": [ ... ]} or {"status":"error", "message": ...}
    """
    try:
        cur = conn.cursor(dictionary=True)

        # Ensure OrganizerFests exists (safe no-op if it already exists)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS OrganizerFests (
                OrgId INT,
                FestId INT,
                Role VARCHAR(50),
                PRIMARY KEY (OrgId, FestId)
            )
        """)

        sql = """
        SELECT f.*
        FROM Fests f
        JOIN OrganizerFests ofst ON ofst.FestId = f.FestId
        WHERE ofst.OrgId = %s
        ORDER BY f.StartDate DESC
        """
        cur.execute(sql, (orgId,))
        rows = cur.fetchall()
        cur.close()
        return {"status": "success", "fests": rows}
    except Exception as e:
        try:
            cur.close()
        except:
            pass
        return {"status": "error", "message": str(e)}

def addArtistToEvent(eventId: int, artistId: int):
    """
    Links an artist to an event.
    Logic:
      - Check if artist and event exist
      - Check duplicates in ArtistEvents
      - Insert if valid and not already linked
    """
    try:
        # 1) Check if event exists
        cursor.execute("SELECT 1 FROM EventsInFest WHERE EventId = %s", (eventId,))
        if cursor.fetchone() is None:
            return {"status": "error", "message": f"Event {eventId} not found."}

        # 2) Check if artist exists
        cursor.execute("SELECT 1 FROM Artists WHERE ArtistId = %s", (artistId,))
        if cursor.fetchone() is None:
            return {"status": "error", "message": f"Artist {artistId} not found in Artists table."}

        # 3) Check duplicate link
        cursor.execute("SELECT 1 FROM ArtistEvents WHERE ArtistId = %s AND EventId = %s", (artistId, eventId))
        if cursor.fetchone():
            return {"status": "exists", "message": "Artist already linked to this event."}

        # 4) Insert link
        cursor.execute("INSERT INTO ArtistEvents (ArtistId, EventId) VALUES (%s, %s)", (artistId, eventId))
        conn.commit()
        return {"status": "success", "message": "Artist linked to event successfully."}

    except Exception as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}


def updateFestInfo(festId: int):
    """
    Show current values side-by-side, prompt for new ones, and update the Fests row.
    Fields handled: FestName, City, StartDate, DescriptionFest.
    """
    try:
        # use a local dict-style cursor for clarity, then close it
        cur = conn.cursor(dictionary=True)

        # 1) fetch existing row
        cur.execute("SELECT FestName, City, StartDate, DescriptionFest FROM Fests WHERE FestId = %s", (festId,))
        row = cur.fetchone()
        if not row:
            cur.close()
            print("Fest not found.")
            return

        # 2) show current values and prompt for new values (enter = keep old)
        print("Leave input blank to keep the current value.\n")
        new_name = input(f"Fest Name [{row['FestName']}]: ").strip()
        new_city = input(f"City [{row['City']}]: ").strip()
        new_date = input(f"Start Date [{row['StartDate']} - YYYY-MM-DD]: ").strip()
        new_desc = input(f"Description [{row['DescriptionFest']}]: ").strip()

        # 3) decide final values (keep old if input blank)
        final_name = new_name if new_name else row['FestName']
        final_city = new_city if new_city else row['City']
        final_date = new_date if new_date else row['StartDate']
        final_desc = new_desc if new_desc else row['DescriptionFest']

        # 4) execute update
        sql = """
            UPDATE Fests
            SET FestName = %s, City = %s, StartDate = %s, DescriptionFest = %s
            WHERE FestId = %s
        """
        conn.start_transaction()
        cur.execute(sql, (final_name, final_city, final_date, final_desc, festId))
        conn.commit()
        cur.close()
        print("Fest updated successfully.")

    except Exception as e:
        try:
            conn.rollback()
        except:
            pass
        try:
            cur.close()
        except:
            pass
        print("Error updating fest:", e)

def festAnalytics(orgId: int):
    """
    Returns aggregated stats for the given organizer:
      - total_fests: number of fests organized by orgId
      - total_events: total events across those fests
      - total_tickets_sold: total tickets sold (count)
      - total_revenue: sum of Tickets.CostPrice
    Returns: {"status":"success","data":{...}} or {"status":"error","message": "..."}
    """
    try:
        cur = conn.cursor(dictionary=True)

        # 1) total fests
        cur.execute("""
            SELECT COUNT(*) AS total_fests
            FROM OrganizerFests
            WHERE OrgId = %s
        """, (orgId,))
        row = cur.fetchone()
        total_fests = int(row['total_fests'] or 0)

        # 2) total events (events belonging to those fests)
        cur.execute("""
            SELECT COUNT(*) AS total_events
            FROM EventsInFest e
            JOIN OrganizerFests ofst ON e.FestId = ofst.FestId
            WHERE ofst.OrgId = %s
        """, (orgId,))
        row = cur.fetchone()
        total_events = int(row['total_events'] or 0)

        # 3) total tickets sold for those fests
        cur.execute("""
            SELECT COUNT(*) AS total_tickets_sold
            FROM Tickets t
            JOIN OrganizerFests ofst ON t.FestId = ofst.FestId
            WHERE ofst.OrgId = %s
        """, (orgId,))
        row = cur.fetchone()
        total_tickets_sold = int(row['total_tickets_sold'] or 0)

        # 4) total revenue (sum of CostPrice)
        cur.execute("""
            SELECT IFNULL(SUM(t.CostPrice), 0) AS total_revenue
            FROM Tickets t
            JOIN OrganizerFests ofst ON t.FestId = ofst.FestId
            WHERE ofst.OrgId = %s
        """, (orgId,))
        row = cur.fetchone()
        # ensure plain Python type
        total_revenue = float(row['total_revenue'] or 0)

        cur.close()
        return {
            "status": "success",
            "data": {
                "total_fests": total_fests,
                "total_events": total_events,
                "total_tickets_sold": total_tickets_sold,
                "total_revenue": total_revenue
            }
        }

    except Exception as e:
        try:
            cur.close()
        except:
            pass
        return {"status": "error", "message": str(e)}


# if __name__ == "__main__":
#     orgId = int(input("Enter Organizer Id: "))
#     n = int(input("How many events to create? "))
#     createFest(orgId, n)

# if __name__ == "__main__":
#     org_id = int(input("Enter Organizer Id to view fests: ").strip())
#     res = viewFestDetails(org_id)
#     if res["status"] == "success":
#         if not res["fests"]:
#             print("No fests found for this organizer.")
#         else:
#             for f in res["fests"]:
#                 print("FestId:", f["FestId"])
#                 print("FestName:", f["FestName"])
#                 print("City:", f.get("City"))
#                 print("StartDate:", f.get("StartDate"))
#                 print("DescriptionFest:", f.get("DescriptionFest"))
#                 print("-" * 40)
#     else:
#         print("Error:", res["message"])

# if __name__ == "__main__":
#     try:
#         event_id = int(input("Enter Event ID: ").strip())
#         artist_id = int(input("Enter Artist ID: ").strip())
#         result = addArtistToEvent(event_id, artist_id)
#         print(result)
#     except Exception as e:
#         print("Error:", e)

# if __name__ == "__main__":
#     fid = int(input("Enter FestId to update: ").strip())
#     updateFestInfo(fid)

if __name__ == "__main__":
    org = int(input("Enter Organizer Id for analytics: ").strip())
    res = festAnalytics(org)
    if res["status"] == "success":
        d = res["data"]
        print("Total fests:", d["total_fests"])
        print("Total events:", d["total_events"])
        print("Total tickets sold:", d["total_tickets_sold"])
        print("Total revenue:", d["total_revenue"])
    else:
        print("Error:", res["message"])


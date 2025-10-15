"""
CrewMembers.py
---------------
Python MySQL connector for Crewmembers table.
All functions use only the Crewmembers table.
"""

import mysql.connector

# ==============================================================
# 🧱 Database Connection
# ==============================================================

conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='as4023755',  # change if needed
    database='Relatify',
    port=3306
)

cursor = conn.cursor()  # tuple-based cursor is fine here

# ==============================================================
# 1️⃣ showMyEvents(memberId)
# ==============================================================

def showMyEvents(memberId: int):
    """
    Since we only have Crewmembers table,
    this shows the member’s profile info.
    """
    try:
        cursor.execute(
            "SELECT Fname, Mname, Lname, City, MemberRole, DOJ FROM Crewmembers WHERE MemberId = %s;",
            (memberId,)
        )
        result = cursor.fetchone()
        if result:
            full_name = " ".join([name for name in result[:3] if name])
            return {
                "FullName": full_name,
                "City": result[3],
                "Role": result[4],
                "DOJ": result[5]
            }
        else:
            return "No such member found."
    except mysql.connector.Error as e:
        return f"MySQL Error: {e}"
    except Exception as e:
        return f"Error: {e}"

# ==============================================================
# 2️⃣ showUpcomingTasks(memberId)
# ==============================================================

def showUpcomingTasks(memberId: int):
    """
    Placeholder: No CrewTasks table.
    """
    try:
        cursor.execute("SELECT MemberRole FROM Crewmembers WHERE MemberId = %s;", (memberId,))
        result = cursor.fetchone()
        if result:
            return f"{result[0]} currently has no assigned tasks."
        else:
            return "Member not found."
    except mysql.connector.Error as e:
        return f"MySQL Error: {e}"
    except Exception as e:
        return f"Error: {e}"

# ==============================================================
# 3️⃣ updateProfile(memberId, newFname, newMname, newLname, newEmail, newPhoneNo, newCity)
# ==============================================================

def updateProfile(memberId: int, newFname: str, newMname: str, newLname: str,
                  newEmail: str, newPhoneNo: str, newCity: str, confirm: bool = True):
    """
    Updates a member’s profile information.
    """
    try:
        query = '''
            UPDATE Crewmembers
            SET Fname=%s, Mname=%s, Lname=%s,
                Email=%s, PhoneNo=%s, City=%s
            WHERE MemberId=%s;
        '''
        cursor.execute(query, (newFname, newMname, newLname, newEmail, newPhoneNo, newCity, memberId))
        if confirm:
            conn.commit()
            if cursor.rowcount == 0:
                return "Update failed. Check MemberId."
            return "Profile updated successfully!"
        else:
            return "Profile update cancelled."
    except mysql.connector.Error as e:
        return f"MySQL Error: {e}"
    except Exception as e:
        return f"Error: {e}"

# ==============================================================
# 4️⃣ changePassword(memberId, oldPass, newPass)
# ==============================================================

def changePassword(memberId: int, oldPass: str, newPass: str, confirm: bool = True):
    """
    Verifies old password and updates to new password.
    """
    try:
        cursor.execute("SELECT AccountPassword FROM Crewmembers WHERE MemberId = %s;", (memberId,))
        record = cursor.fetchone()
        if not record:
            return "Member not found."

        stored_pass = record[0]
        if stored_pass != oldPass:
            return "Incorrect old password."

        if confirm:
            cursor.execute("UPDATE Crewmembers SET AccountPassword=%s WHERE MemberId=%s;", (newPass, memberId))
            conn.commit()
            if cursor.rowcount == 0:
                return "Password update failed. Check MemberId."
            return "Password changed successfully!"
        else:
            return "Password change cancelled."
    except mysql.connector.Error as e:
        return f"MySQL Error: {e}"
    except Exception as e:
        return f"Error: {e}"

# ==============================================================
# 5️⃣ taskStats(memberId)
# ==============================================================

def taskStats(memberId: int):
    """
    Returns basic info summary since no CrewTasks table exists.
    """
    try:
        cursor.execute("SELECT Fname, Lname, MemberRole, DOJ FROM Crewmembers WHERE MemberId=%s;", (memberId,))
        member = cursor.fetchone()
        if member:
            return {
                "Name": f"{member[0]} {member[1]}",
                "Role": member[2],
                "DOJ": member[3],
                "TasksCompleted": 0,
                "TasksPending": 0
            }
        else:
            return "Member not found."
    except mysql.connector.Error as e:
        return f"MySQL Error: {e}"
    except Exception as e:
        return f"Error: {e}"

# ==============================================================
# 🧪 Testing
# ==============================================================

if __name__ == "__main__":
    print("\n🧩 showMyEvents()")
    print(showMyEvents(1))

    print("\n🧩 showUpcomingTasks()")
    print(showUpcomingTasks(1))

    print("\n🧩 updateProfile()")
    print(updateProfile(1, 'Ravi', 'K.', 'Sharma', 'ravi@example.com', '9998887770', 'Pune'))

    print("\n🧩 changePassword()")
    print(changePassword(1, 'oldpass', 'newpass123'))

    print("\n🧩 taskStats()")
    print(taskStats(1))

    cursor.close()
    conn.close()

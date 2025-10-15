import mysql.connector
from datetime import date


conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='Relatify',
    port=3306
)
cursor = conn.cursor(dictionary=True) 

def showMyEvents(artistId: int):
    """
    Fetch upcoming events for the artist.
    Joins ArtistEvents, EventsInFest, Fests.
    Filters events with EventDate >= today.
    """
    query = '''
        SELECT EventsInFest.EventId, EventsInFest.EventName, EventsInFest.EventDate, EventsInFest.EventTime, Fests.FestName, Fests.City
        FROM ArtistEvents
        JOIN EventsInFest ON ArtistEvents.EventId = EventsInFest.EventId
        JOIN Fests ON EventsInFest.FestId = Fests.FestId
        WHERE ArtistEvents.ArtistId = %s AND EventsInFest.EventDate >= CURDATE()
        ORDER BY EventsInFest.EventDate ASC;
    '''
    cursor.execute(query, (artistId,))
    return cursor.fetchall()

def showFavCount(artistId: int):
    """
    Returns number of users who marked artist as favourite.
    """
    query = '''
        SELECT COUNT(*) as FavCount
        FROM UserFavourites
        WHERE ArtistId = %s;
    '''
    cursor.execute(query, (artistId,))
    result = cursor.fetchone()
    return result['FavCount'] if result else 0

def updateContractFee(artistId: int, newFee: float, password: str):
    """
    Updates contract fee after verifying artist password.
    """
    try:
        # Verify password
        cursor.execute("SELECT AccountPassword FROM Artists WHERE ArtistId = %s;", (artistId,))
        result = cursor.fetchone()
        if not result or result['AccountPassword'] != password:
            return "Password incorrect. Fee update failed."

        # Update contract fee
        cursor.execute("UPDATE Artists SET ContractFee = %s WHERE ArtistId = %s;", (newFee, artistId))
        conn.commit()
        return "Contract fee updated successfully."
    except Exception as e:
        conn.rollback()
        return f"Error occurred: {e}"

def showMyInfo(artistId: int, role=None):
    """
    Returns artist’s profile as dictionary.
    If role is 'user', removes sensitive fields.
    """
    cursor.execute("SELECT * FROM Artists WHERE ArtistId = %s;", (artistId,))
    artist_info = cursor.fetchone()
    if not artist_info:
        return {}

    if role == 'user':
        # Hide sensitive fields
        artist_info.pop('ContractFee', None)
        artist_info.pop('AccountPassword', None)
        artist_info.pop('Email', None)

    return artist_info

#testing
if __name__ == "__main__":
    artist_id = 3

    print("Upcoming Events for Artist:")
    for event in showMyEvents(artist_id):
        print(event)

    print("\nFavourite Count:")
    print(showFavCount(artist_id))

    print("\nUpdate Contract Fee:")
    print(updateContractFee(artist_id, 25000.0, "pass123"))

    print("\nShow Artist Info (Admin):")
    print(showMyInfo(artist_id))

    print("\nShow Artist Info (User):")
    print(showMyInfo(artist_id, role='user'))

import mysql.connector

conn = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'Waheguru1313_',
    database = 'Relatify',
    port = 3306
)

cursor = conn.cursor()

def UserFavArtistsFests(userId : int):
    
    query = f'''SELECT Fests.* FROM ( SELECT * FROM  ( SELECT EventId FROM (
                        SELECT ArtistId 
                        FROM UserFavourites 
                        WHERE UserId = %s
                    ) AS Temp NATURAL JOIN ArtistEvents
                ) AS TempEvent NATURAL JOIN EventsInFest
            ) AS TempFest NATURAL JOIN Fests;'''
            
    cursor.execute(query, (userId, ))
    outputs = cursor.fetchall()
    
    fests = set(outputs)
    return fests

def UserCityFests(userId : int):
    
    query = f'''SELECT Fests.* FROM Fests NATURAL JOIN (SELECT City FROM Users WHERE UserId = %s) AS Temp;'''
    
    cursor.execute(query, (userId, ))
    outputs = cursor.fetchall()
    
    fests = set(outputs)
    
    return fests

def listFests(userId : int):
    
    '''This function returns a tuple of list with:
    
    1. List of Fests where user with user Id Favourite artists
    are performing
    
    2. List of Fests that are going to be organized in user\'s city
    
    3. List of all fests except the fests listed above'''
    
    userFavArtFests = UserFavArtistsFests(userId)
    usercityFests = UserCityFests(userId)
    
    query = '''SELECT * FROM Fests;'''
    
    cursor.execute(query)
    outputs = cursor.fetchall()
    
    fests = set(outputs) - usercityFests - userFavArtFests
        
    return userFavArtFests, usercityFests, fests

def ticketsPurchased(userId : int):
    
    query = '''SELECT DISTINCT Fests.FestName, Fests.City, Tickets.PurchaseDate, Tickets.Tier, Tickets.CostPrice 
            FROM Tickets 
            JOIN Fests ON Fests.FestId = Tickets.FestId
            WHERE UserId = %s;'''
            
    cursor.execute(query, (userId, ))
    outputs = set(cursor.fetchall())
    
    return outputs, len(outputs)

def festUserAttended(userId : int):
    
    query = '''SELECT Fests.*
        FROM UserFests
        JOIN Fests ON Fests.FestId = UserFests.FestId
        WHERE UserId = %s;'''
        
    cursor.execute(query, (userId, ))
    outputs = set(cursor.fetchall())
    
    return outputs, len(outputs)

def addArtistFav(userId: int, artistId: int, confirm: bool):
    try:
        conn.start_transaction()
        query = "INSERT INTO UserFavourites (UserId, ArtistId) VALUES (%s, %s)"
        cursor.execute(query, (userId, artistId))
        
        if confirm:
            conn.commit()
            return "Artist added to favourites successfully!"
        else:
            conn.rollback()
            return "Action cancelled. No changes made."
            
    except Exception as e:
        conn.rollback()
        return f"Error: {e}"
    
def removeFromFav(userId: int, artistId: int, confirm: bool):
    try:
        cursor.execute('SELECT * FROM UserFavourites WHERE UserId = %s AND ArtistId = %s;', (userId, artistId))
        outputs = cursor.fetchall()
        
        if not outputs:
            return "No artist was found in your favourites."
        
        conn.start_transaction()
        cursor.execute('DELETE FROM UserFavourites WHERE UserId = %s AND ArtistId = %s;', (userId, artistId))
        
        if confirm:
            conn.commit()
            return "Artist removed from your favourites list."
        else:
            conn.rollback()
            return "No artist was removed from your favourites list."
    
    except Exception as e:
        conn.rollback()
        return f"An error occurred: {e}"

def changeUserName(userId : int, userName : str, newUserName : str, password : str, confirm : bool):
    
    try:
        queryForPass = '''SELECT Password FROM Users WHERE UserId = %s;'''
        cursor.execute(queryForPass)
        passW = cursor.fetchall()[0]
        
        if passW == password:
            
            userNameChgQuery = '''UPDATE Users SET UserName = %s WHERE UserId = %s;'''
            
            conn.start_transaction()
            cursor.execute(userNameChgQuery, (newUserName, userId))
            
            if confirm:
                conn.commit()
                return "User Name Changed!!"
            else:
                conn.rollback()
                return "User Name not Changed!!"
            
        else:
            return "Wrong Password"
        
    except Exception as e:
        conn.rollback()
        return "An error occured!!"

if __name__ == "__main__":
    
    print("Testing function : UserFavArtistsFests")
    for r in UserFavArtistsFests(userId = 7):
        for rows in r:
            print(rows)
    
    print("\nTesting function : UserCityFests")
    for r in UserCityFests(userId = 7):
        for rows in r:
            print(rows)
    
    print("\nTesting function : listFests")
    for r in listFests(userId = 7):
        for rows in r:
            print(rows)
        print()
    
    print("\nTesting function : ticketsPurchased") 
    
    funcOP = ticketsPurchased(userId = 7)
    for rows in funcOP[0]:
        print(rows)
        
    print("\nTesting function : festUserAttended")
    
    funcOP = festUserAttended(userId = 7)
    for rows in funcOP[0]:
        print(rows)
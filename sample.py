#You Must first install mysql.connector in your system, for this execute following query
#pip install mysql-connector-python

import mysql.connector

#Setting up connection with MySQL servers
conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = 'root',
    database = 'Relatify',
    password = 'ENTER YOUR ACCOUNT PASSWORD HERE',
    port = 3306
)

#Creating a cursor object
cursor = conn.cursor()

#.execute is used for executing queries
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()

for r in rows:
    print(r)

#closing connection with cursor
cursor.close()
conn.close()
import mysql.connector

friendsDB = mysql.connector.connect (
    host="localhost",
    user="testuser",
    passwd="Testuserpassword123!",
    database="Friends"
)

c = friendsDB.cursor()
#c.execute("CREATE DATABASE Friends")
#c.execute("USE Friends")

#c.execute("CREATE TABLE Friends (FirstName VARCHAR(255), LastName VARCHAR(255), Closeness INT)")

query = "INSERT INTO friends (FirstName, LastName, Closeness) VALUES (%s, %s, %s)"
data = ("Matt", "Brown", "9")
c.execute(query, data)
friendsDB.commit()

for friend in c:
    print(friend)

friendsDB.close()
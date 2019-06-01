import mysql.connector

friendsDB = mysql.connector.connect (
    host="localhost",
    user="testuser",
    passwd="Testuserpassword123!",
    database="Friends"
)

c = friendsDB.cursor()

c.execute("SELECT * FROM Friends WHERE FirstName = 'Matt'")

print(c.fetchall())

friendsDB.commit()
friendsDB.close()
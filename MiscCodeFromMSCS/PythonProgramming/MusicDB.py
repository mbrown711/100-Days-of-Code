import mysql.connector

musicDB = mysql.connector.connect (
    host="localhost",
    user="***",
    passwd="***"
)
#obviously don't need all of these, but good way to learn what each execute is doing
myCursor = musicDB.cursor()
useCursor = musicDB.cursor()
createCursor = musicDB.cursor()
createTableCursor = musicDB.cursor()
showTablesCursor = musicDB.cursor()

# createCursor.execute("CREATE DATABASE Music")

useCursor.execute("USE Music")

myCursor.execute("SHOW DATABASES")

for x in myCursor:
    print(x)

createTableCursor.execute("CREATE TABLE Customers (name VARCHAR(255), Address VARCHAR(225))")

showTablesCursor.execute("SHOW TABLES")

for table in showTablesCursor:
    print(table)
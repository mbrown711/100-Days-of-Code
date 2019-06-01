import mysql.connector

friendsDB = mysql.connector.connect (
    host="localhost",
    user="testuser",
    passwd="Testuserpassword123!",
    database="Friends"
)

c = friendsDB.cursor()

people = [
    ("Dalila", "Castillo", 4),
    ("Chris", "Brown", 7),
    ("Kelly", "Brown", 8),
    ("Alicia", "Brown", 7),
    ("Tim", "Brown", 6)
]

c.executemany("INSERT INTO Friends (FirstName, LastName, Closeness) VALUES (%s, %s, %s)", people)

average = 0
for person in people:
    average += person[2]

print(average/len(people))

friendsDB.commit()
friendsDB.close()
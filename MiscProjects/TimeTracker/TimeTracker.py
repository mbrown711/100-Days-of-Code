# Assuming that there is an existing database, connect to it.

import mysql.connector

timeTrackerDB = mysql.connector.connect (
    host="localhost",
    user="testuser",
    passwd="Testuserpassword123!",
    database="Time_Tracker"
)

# Create a new table unless it already exists (which I'm assuming it does already)

createTable = "CREATE TABLE IF NOT EXISTS Employees (Id INT NOT NULL AUTO_INCREMENT, FirstName VARCHAR(255), LastName VARCHAR(255), Clock_In TIME, Clock_Out TIME, PRIMARY KEY (Id))"

c = timeTrackerDB.cursor()

# Creating table for employees, showing clocking in and out:
c.execute(createTable)

# Inserting some test data:
employees = [
    (1, "Homer", "Simpson", '08:00:00', '10:00:00'),
    (2, "Ned", "Flanders", '13:00:00', '18:00:00'),
    (3, "Seymour", "Skinner", '15:00:00', '20:00:00'),
    (4, "Moe", "Szyslak", '21:00:00', '01:30:00'),
    (5, "Troy", "McClure", '12:00:00', '15:00:00')
]

insertMany = "INSERT INTO Employees (Id, FirstName, LastName, Clock_In, Clock_Out) VALUES (%s, %s, %s, %s, %s)"

c.executemany(insertMany, employees)

timeTrackerDB.commit()

# Creating the even in MySQL to run the report once every two weeks:
createEvent = "CREATE EVENT IF NOT EXISTS get_times ON SCHEDULE EVERY 2 WEEK STARTS CURRENT_DATE DO SELECT * FROM Employees"

c.execute(createEvent)

# If we need to export the file into a csv, we can add that as well.

timeTrackerDB.commit()
timeTrackerDB.close()
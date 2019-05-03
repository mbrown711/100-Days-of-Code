package com.mattbrown;

import java.sql.*;

public class Main {

    public static void main(String[] args) {

	    try {
	        // if a db doesn't exist, sqlite will create one for you
            Connection conn = DriverManager.getConnection("jdbc:sqlite:/Users/macbook/GoogleDrive/Programming/100DaysOfCode/Udemy/JavaMasterclass/JDBCPracticeWithSQLite/testjava.db");
            //conn.setAutoCommit(false);
            Statement statement = conn.createStatement();
            statement.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)");
            statement.execute("INSERT INTO contacts(name, phone, email) VALUES ('Matt', 7818645115, 'matt@email.com')");
            statement.execute("INSERT INTO contacts(name, phone, email) VALUES ('Dalila', 2017240767, 'dalila@anotheremail.com')");
            statement.execute("INSERT INTO contacts(name, phone, email) VALUES ('Bailey', 1234567890, 'bailey@barkbark.com')");
            statement.execute("INSERT INTO contacts(name, phone, email) VALUES ('Mom', 7894561230, 'mom@bestmom.com')");
            statement.execute("UPDATE contacts SET phone = 4563217890 WHERE name = 'Dalila'");
            statement.execute("DELETE FROM contacts WHERE name = 'Matt'");

            statement.execute("SELECT * FROM contacts");
            ResultSet results = statement.getResultSet();
            while(results.next()) {
                System.out.println(results.getString("name") + " " + results.getInt("phone") + " " + results.getString("email"));
            }

            results.close();
            statement.close();
            conn.close();
        } catch(SQLException e) {
            System.out.println("Error from try catch block for SQLException e: " + e.getMessage());
        }
    }
}

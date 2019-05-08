package com.mattbrown;

import java.sql.*;

public class Main {
    //JDBC driver name and database URL:
    static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
    static final String DB_URL = "jdbc:mysql://localhost:3306";

    //database credentials:
    static final String USER = "testuser";
    static final String PASSWORD = "Testuserpassword123!";

    public static void main(String[] args) {

        Connection connection = null;
        Statement statement = null;

        try {
            //register JDBC driver:
            Class.forName(JDBC_DRIVER);
            //open a connection:
            System.out.println("Connecting to database...");
            connection = DriverManager.getConnection(DB_URL, USER, PASSWORD);
            //execute a query:
            System.out.println("Creating a statement...");
            statement = connection.createStatement();
            String dbUse = "USE test_db";
            ResultSet use = statement.executeQuery(dbUse);
            String sqlQuery = "SELECT id, name, surname, age FROM NameTable";
            ResultSet resultSet = statement.executeQuery(sqlQuery);

            //extract data from resultSet:
            while (resultSet.next()) {
                //retrieve by column name:
                int id = resultSet.getInt("id");
                int age = resultSet.getInt("age");
                String name = resultSet.getString("name");
                String surname = resultSet.getString("surname");

                //display values:
                System.out.println("ID: " + id);
                System.out.println("Age: " + age);
                System.out.println("First name: " + name);
                System.out.println("Last name: " + surname);
            }
            resultSet.close();
            statement.close();
            connection.close();

        } catch (SQLException sqlE) {
            //handle errors for JDBC:
            sqlE.printStackTrace();
        } catch (Exception e) {
            //handle errors for class.forname:
            e.printStackTrace();
        } finally {
            //finally block used to close resources:
            try {
                if (statement != null) {
                    statement.close();
                }
            } catch (SQLException se2) {
                //nothing
            }
            try {
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException se) {
                se.printStackTrace();
            }
        } //end finally try
    }
}
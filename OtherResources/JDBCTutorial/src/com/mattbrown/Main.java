package com.mattbrown;

import java.sql.*;

public class Main {

    private static final String URL = "jdbc:mysql://localhost/";
    private static final String DB = "PaperReviews";
    private static final String USER = "testuser";
    private static final String PASSWORD = "Testuserpassword123!";

    public static void main(String[] args) {

        String sqlQuery = "SELECT * FROM paper WHERE Id = 3";
        //String sqlInsert = "INSERT INTO name_table (name, surname, age) VALUES (?, ?, ?)";

        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection conn = DriverManager.getConnection(URL + DB, USER, PASSWORD);

            PreparedStatement preparedStatement = conn.prepareStatement(sqlQuery);
            //preparedStatement.setString(1, "Jones"); <-- use to select a particular instance
            ResultSet results = preparedStatement.executeQuery();

//            PreparedStatement preparedInsert = conn.prepareStatement(sqlInsert);
//            String myName = "Matt";
//            String mySurname = "Brown";
//            int myAge = 29;

//            preparedInsert.setString(1, myName);
//            preparedInsert.setString(2, mySurname);
//            preparedInsert.setInt(3, myAge);

            //int status = preparedInsert.executeUpdate();
            //System.out.println(status);

            while (results.next()) {
                int paperId = results.getInt(1);
                String title = results.getString(2);
                String abstractText = results.getString(3);
                String fileName = results.getString(4);

                System.out.printf("%d\t%s\t%s\t%s\n", paperId, title, abstractText, fileName);
            }

        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }

    }
}
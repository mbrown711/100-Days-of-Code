import java.sql.*;

public class MethodsForSQLInsertion {

    public static final String DB_NAME = "testjava.db";
        public static final String CONNECTION_STRING = "jdbc:sqlite:/Users/macbook/GoogleDrive/Programming/100DaysOfCode/Udemy/JavaMasterclass/JDBCPracticeWithSQLite/" +DB_NAME;

        public static final String TABLE_CONTACTS = "contacts";

        public static final String COLUMN_NAME = "name";
        public static final String COLUMN_PHONE = "phone";
        public static final String COLUMN_EMAIL = "email";
    public static void main(String[] args) {

        try {
            Connection conn = DriverManager.getConnection(CONNECTION_STRING);
            Statement statement = conn.createStatement();
            statement.execute("DROP TABLE IF EXISTS " + TABLE_CONTACTS);
            statement.execute("CREATE TABLE IF NOT EXISTS " + TABLE_CONTACTS + " (" + COLUMN_NAME + " text, " + COLUMN_PHONE + " integer, " + COLUMN_EMAIL + " text" + ")");

            statement.execute("INSERT INTO " + TABLE_CONTACTS + " (" + COLUMN_NAME + ", " + COLUMN_PHONE + ", " + COLUMN_EMAIL + " ) " + "VALUES('Matt', 7818645115, 'matt@email.com')");

            statement.execute("INSERT INTO " + TABLE_CONTACTS + " (" + COLUMN_NAME + ", " + COLUMN_PHONE + ", " + COLUMN_EMAIL + " ) " + "VALUES('Dalila', 7362718273, 'dalila@google.com')");

            statement.execute("INSERT INTO " + TABLE_CONTACTS + " (" + COLUMN_NAME + ", " + COLUMN_PHONE + ", " + COLUMN_EMAIL + " ) " + "VALUES('Bailey', 8746388222, 'bailey@barkbark.com')");

            statement.execute("UPDATE " + TABLE_CONTACTS + "SET " + COLUMN_PHONE + " = 6444444444" + " WHERE " + COLUMN_NAME + " = Dalila");

            statement.execute("DELETE FROM " + TABLE_CONTACTS + " WHERE" + COLUMN_NAME + " = 'Matt'");

            ResultSet results = statement.executeQuery("SELECT * FROM " + TABLE_CONTACTS);
            while(results.next()) {
                System.out.println(results.getString(COLUMN_NAME) + " " + results.getString(COLUMN_PHONE) + " " + results.getString(COLUMN_EMAIL));
            }

            results.close();
            statement.close();
            conn.close();

        } catch(SQLException e) {
            System.out.println("Error from try catch block for SQLException e: " + e.getMessage());
            e.printStackTrace();
        }
    }
    //below are example/practice methods to use for the DBMS java project
    private static void insertContact(Statement statement, String name, int phone, String email) {
        
    }
}
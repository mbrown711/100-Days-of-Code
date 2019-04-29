package com.example.sqltest;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        SQLiteDatabase sqLiteDatabase = openOrCreateDatabase("sqlite-test-1.db", MODE_PRIVATE, null);
        String sql = "DROP TABLE IF EXISTS contacts;";
        sqLiteDatabase.execSQL(sql);
        // pass a string to execute the sql statements
        sqLiteDatabase.execSQL("CREATE TABLE contacts(name TEXT, phone INTEGER, email TEXT)");
        // this inserts the data into the table we just created above
        sqLiteDatabase.execSQL("INSERT INTO contacts VALUES('Matt', 7818645115, 'matt@email.com')");
        sqLiteDatabase.execSQL("INSERT INTO contacts VALUES('Dalila', 2017240767, 'dalila@email.com')");

        // write code to retrieve the code to make sure the data is write
        // use a cursor for this - points to single row at a time
        // avoids performance issues if there are thousand of entries

        Cursor query = sqLiteDatabase.rawQuery("SELECT * FROM contacts;", null);
        // query is a cursor and we're telling it to move to the first record
        // reading the values for the first record below; need to use index 0 as the first one
        if (query.moveToFirst()) {
            // below loop adds each insert into from above
            // need to execute at least once, so we use a do..while loop
            do {
                String name = query.getString(0);
                int phone = query.getInt(1);
                String email = query.getString(2);
                Toast.makeText(this, "Name = " + name + "Phone = " + phone + "Email = " + email, Toast.LENGTH_LONG).show();
            } while (query.moveToNext());
        }
        // closing cursor and DB when we're done with it
        // this is good in order for freeing up resources & garbage collection
        query.close();
        // close the DB when the app itself is closed
        sqLiteDatabase.close();

        FloatingActionButton fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}

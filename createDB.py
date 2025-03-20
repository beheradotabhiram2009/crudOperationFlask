import sqlite3

conn = sqlite3.connect('sqlite.db')
print ("Opened database successfully");

conn.execute('CREATE TABLE students (rollno TEXT primary key, name TEXT not null, branch TEXT, phone TEXT, email TEXT, dob DATE)')
print ("Table created successfully");
conn.close()

## crudOperationFlask
crud operation using Flask and sqlite
### create a new folder crudProject open the folder in vscode
### To check pip version, type the following command
``` C:\Users\username> python -m pip –version ```
### To Check the version of Python installed in your system, run
``` C:\Users\username> python –V ```
### Now, use the following command to install Flask
```
pip install flask
```
### Now, use the following command to install Sqlite3
```
pip install db-sqlite3
```
### Install Python debugger and Sqlite DB explorer
### Write the following program in app.py in your project folder
```
from flask import Flask, render_template  
import sqlite3 as sql

app = Flask(__name__)   # Flask constructor 

# A decorator used to tell the application 
# which URL is associated function 

@app.route('/')       
def hello(): 
    funda = ['funda','of','web','IT']
    data = "3214"
    context = {'data':data, 'funda':funda}
    return render_template("index.html", context=context)

if __name__=='__main__': 
   app.run(debug=True) 
```
### Create templates folder under project folder and create a file  index.html under template folder with following code
```
<html>
<body>
    <h1>This is a HTML page</h1>
    <h1>{{context.data}}</h1>
    <p>This is a paragraph tag</p>
    
    {% for info in context.funda %} <!-- info is the variable name-->
        {{info}} <br>
    {% endfor %}
</body>
</html>
```
### Run the app.py and browse the page :
```
http://127.0.0.1:5000
```
### To create database write following code in created.py and run it
```
import sqlite3

conn = sqlite3.connect('sqlite.db')
print ("Opened database successfully");

conn.execute('CREATE TABLE students (rollno TEXT primary key, name TEXT not null, branch TEXT, phone TEXT, email TEXT, dob DATE)')
print ("Table created successfully");
conn.close()
```
### To add sample data we can use installed DB Browser for (SQLite) on the system and  to create a sql file in vscode use command ctrl shift p
### select sqlite: New Query
### select the db.sqlite3 database
### type the insert query
```
insert into students (rollno, name, branch, phone, email, dob) values
('101', 'rama', 'cse', '8895955560', 'behera.abhiram2009@gmail.com', '1972-06-14')
```
### To run the Query Type  ctrl shift p
### select sqlite: Run Query
### To check if inserted, write in sql file and run
```
SELECT * from students
```
### On right side we can see the result
### To show student Data write  function in app.py
```
import sqlite3 as sql

@app.route('/students/student_list')
def student_list():
   con = sql.connect("sqlite.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall(); 
   con.close();
   return render_template("students/index.html", rows = rows)
```
### Create students folder under templates and add index.html file under it
```
<html>
    <head>
        <style>
            .evenrow{ background-color:bisque; }
            .oddrow { background-color: rgb(222, 217, 217); }
        </style>
    </head>
    <body>
    <div align="center">
    <table cellspacing="0" cellpadding="10" border="0">
        <thead><h2 style="color: #1da85b;"><u>Student List</u></h2></thead>
        <thead align="left"><th ><a href="./student_entry" ><input type="button" value="Add Student" /></a></th></thead>
        <thead style="background-color: rgb(92, 67, 139); color: #f7f8f9;">
            <tr>
                <th scope="col">Roll No</th>
                <th scope="col">Name</th>
                <th scope="col">Branch</th>
                <th scope="col">phone</th>
                <th scope="col">email</th>
                <th scope="col">DOB</th>
                <th scope="col">Edit</th>
                <th scope="col">Delete</th>
            </tr>
        </thead>
        {% for info in rows %} 
        <tr class="{{ loop.cycle('oddrow', 'evenrow') }}">
            <td>  {{info["rollno"]}} </td>
            <td>  {{info["name"]}}   </td>
            <td>  {{info["branch"]}} </td>
            <td>  {{info["phone"]}}  </td>
            <td>  {{info["email"]}}  </td>
            <td>  {{info["dob"]}}  </td>
            <td><a href="./edit_student/{{info['rollno']}}"><input type="button" value="Edit"/></a></td>
            <td><a href="./delete_student/{{info['rollno']}}"><input type="button" value="Delete"/></a></td>
        </tr>
        {% endfor %}
    </table>
    </div>
    </body>
</html>
```
### Run app.py and check in  browser 
```
http://127.0.0.1:5000/students/student_list
```
### To Add students create student_entry and add_student functions in app.py
```
@app.route('/students/student_entry')
def student_entry():
    form = []
    context = {'form':form}
    return render_template('students/insert_student.html', context=context)

@app.route('/students/add_student',methods = ['POST', 'GET'])
def add_student():
   if request.method == 'POST':
      rno = request.form['rollno']
      nm = request.form['name']
      br= request.form['branch']
      ph = request.form['phone']
      mail = request.form['email']
      db = request.form['dob']

      con = sql.connect("sqlite.db")
      cur = con.cursor()
      cur.execute("INSERT INTO students (rollno, name, branch, phone, email, dob) \
            VALUES (?,?,?,?,?,?)",(rno, nm, br, ph, mail, db) )
      con.commit()
      con.close()
      return redirect('/students/student_list')
```
### Under templates/students folder create insert_student.html  file 
```
<html><body><div align="center">
    <h2 style="color: #1da85b;"><u>Enter Student Data To Insert</u></h2>
    <form action="add_student" method="post">
   <fieldset style="width: 500;">            
      <legend>Insert Student data here</legend>
        <table style="color: #9a1fa5;" cellspacing="5" cellpadding="5">
            <tr>
                <td><label for="rollno">Roll No: </label></td>
                <td><input id="rollno" type="text" name="rollno"></td>
            </tr>
            <tr>
                <td><label for="name">Name: </label></td>
                <td><input id="name" type="text" name="name"></td>
            </tr>
            <tr>
                <td><label for="branch">Branch: </label></td>
                <td><input id="branch" type="text" name="branch"></td>
            </tr>
            <tr>
                <td><label for="email">Email: </label></td>
                <td><input id="email" type="text" name="email"></td>
            </tr>
            <tr>
                <td><label for="phoneno">Phone Number: </label></td>
                <td><input id="phone" type="text" name="phone"></td>
            </tr>
            <tr>
                <td><label for="dob">Date of Birth: </label></td>
                <td><input id="dob" type="date" name="dob"></td>
            </tr>
            <tr align="left">
                <td></td>
                <td>
                    <input type="submit" value="Insert">
                    <a href="."><input type="button" value="Cancel"/></a>
                </td>
            </tr>
        </table>
        </fieldset>
</form></div></body></html>
```
### Run app.py and check insertion in browser
### To provide delete operation  create  delete_student  function in app.py
```
@app.route('/students/delete_student/<rno>')
def delete_student(rno):   
      con = sql.connect("sqlite.db")
      cur = con.cursor()
      cur.execute("delete from students where rollno=?",(rno,))
      con.commit()
      con.close()
      return redirect('/students/student_list')
```
### Check delete operation by running app.py and browsing
### To provide Edit operation  create edit_student, update_student functions in app.py
```
@app.route('/students/edit_student/<rno>')
def edit_student(rno):
    con = sql.connect("sqlite.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM students WHERE rollno = ?', (rno,))
    thestudent = cur.fetchone()
    con.close()
    return render_template('/students/edit_student.html', thestudent=thestudent)

@app.route('/students/edit_student/update_student/<rno>',methods = ['POST', 'GET'])
def update_student(rno):
   if request.method == 'POST':
      nm = request.form['name']
      br= request.form['branch']
      ph = request.form['phone']
      mail = request.form['email']
      db = request.form['dob']

      con = sql.connect("sqlite.db")
      cur = con.cursor()
      cur.execute('update students SET name = ?, branch = ?, phone = ?, email = ?, dob = ?' 
                    ' WHERE rollno = ?',(nm, br, ph, mail, db, rno) )
      con.commit()
      con.close()
      return redirect('/students/student_list')     

if __name__=='__main__': 
   app.run(debug=True) 
```
### Now create template edit.html under templates/students
```
<html>
    <body>
        <h2 style="color: #1da85b;" align="center"><u>Edit Student Data</u></h2>
        <div align="center">
        <form action="update_student/{{thestudent['rollno']}}" method="post">
          <fieldset style="width: 500;">
            <legend>Edit Student data here</legend>
            <table style="color: #9a1fa5;" cellspacing="5" cellpadding="5">
                <tr>
                    <td><label for="name">Name: </label></td>
                    <td><input id="name" type="text" name="name" value="{{thestudent['name']}}"></td>
                </tr>
                <tr>
                    <td><label for="branch">Branch: </label></td>
                    <td><input id="branch" type="text" name="branch" value="{{thestudent['branch']}}"></td>
                </tr>
                <tr>
                    <td><label for="email">Email: </label></td>
                    <td><input id="email" type="text" name="email" value="{{thestudent['email']}}"></td>
                </tr>
                <tr>
                    <td><label for="phoneno">Phone Number: </label></td>
                    <td><input id="phone" type="text" name="phone" value="{{thestudent['phone']}}"></td>
                </tr>
                <tr>
                    <td><label for="dob">Date of Birth: </label></td>
                    <td><input id="dob" type="date" name="dob" 
                        value="{{thestudent['dob']}}"></td>
                </tr>
                <tr align="left">
                    <td></td>
                    <td>
                        <input type="submit" value="Update"/>
                        <a href="../"><input type="button" value="Cancel"/></a>
                    </td>
                </tr>
            </table>
            </fieldset>
        </form>
        </div>
        </body>
        </body>
    </body>
</html>
```
### Run app.py check edit browsing the page

from flask import Flask, render_template, request, redirect  
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

@app.route('/students/student_list')
def student_list():
   con = sql.connect("sqlite.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall(); 
   con.close();
   return render_template("students/index.html", rows = rows)

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

@app.route('/students/delete_student/<rno>')
def delete_student(rno):   
      con = sql.connect("sqlite.db")
      cur = con.cursor()
      cur.execute("delete from students where rollno=?",(rno,))
      con.commit()
      con.close()
      return redirect('/students/student_list')

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
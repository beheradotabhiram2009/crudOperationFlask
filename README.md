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

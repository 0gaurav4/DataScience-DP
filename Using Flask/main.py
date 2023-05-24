from flask import Flask, render_template, request
from database import Laptop
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# initilization flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

Base = declarative_base

def connectDatabase():
    pass

@app.route('/')
@app.route('/home')
def index():
    mongo.db.inventor.insert_one({"a": 1})
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        data = request.form
        print(data)
    return render_template('register.html')

@app.route('/display')
def displayData():
    
    myname = "Gaurav"
    fruits = ['Apple','Pineapple', 'Orange', 'Grapes']
    return render_template('view.html', name=myname, fruit_data=fruits)

app.run(debug=True, port=5002)
#!/usr/bin/python3
"""web frame work module"""

from flask import Flask, render_template, url_for, json, request
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from mysql.connector import connect, Error
from getpass import getpass
import mysql.connector as myconn


app = Flask(__name__)


#mysql = MySQL()
#MySQL configurations 
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = ''
#app.config['MYSQL_DATABASE_DB'] = 'ecommerce_store'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)


#conn = mysql.connect()
#cursor = conn.cursor()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("About.html")

@app.route("/gallery/")
def gallery():
    return render_template("Gallery.html")

@app.route("/signup/")
def signup():
    return render_template('signup.html')

@app.route('/api/signup',methods=['POST'])
def signUp():
    mydb = myconn.connect(
        host = "localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database = "ecommerce_store"
        )
obj = mydb.cursor()
obj.callproc("sp_createUser", [f_name, l_name, email, phone, password])

for result in obj.stored_results():
    details = result.fetchall()

for det in details:
    print(det)

obj.close()
mydb.close()
    

    # create user code will be here !!
    f_name = request.form['inputName']
    l_name = request.form['inputName']
    email = request.form['inputEmail']
    phone = request.form['inputPhone']
    password = request.form['inputPassword']
    
    # validate the received values
    if f_name and l_name and email and phone and password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

    hashed_password = generate_password_hash(_password)
    cursor.callproc('sp_createUser',(f_name,l_name,email,phone,hashed_password))
    data = cursor.fetchall()
    
    if len(data) == 0:
        conn.commit()
        return json.dumps({'message':'User created successfully !'})
    else:
        return json.dumps({'error':str(data[0])})


if __name__ == "__main__":
    app.run(debug=True)

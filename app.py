#!/usr/bin/python3
"""web frame work module"""

from flask import Flask, render_template, url_for
from getpass import getpass
from mysql.connector import connect, Error

app = Flask(__name__)

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        print(connection)
except Error as e:
    print(e)


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

if __name__ == "__main__":
    app.run(debug=True)

#!/usr/bin/python3
"""web frame work module"""

from flask import Flask, render_template, url_for
from getpass import getpass
from mysql.connector import connect, Error

app = Flask(__name__)
customers = """
CREATE TABLE IF NOT EXISTS customers (cust_id INT (11) PRIMARY KEY AUTO_INCREMENT, f_name VARCHAR (30) NOT NULL,
l_name VARCHAR(30) NOT NULL, email VARCHAR(30), phone VARCHAR(30) NOT NULL)"""

products_table = """
CREATE TABLE IF NOT EXISTS products (prod_id INT (11) PRIMARY KEY AUTO_INCREMENT, prod_name VARCHAR (30), prod_price DECIMAL (4, 2)
)
"""

orders_table = """
    CREATE TABLE IF NOT EXISTS orders (order_id INT (11) PRIMARY KEY AUTO_INCREMENT, FOREIGN KEY (cust_id) REFERENCES customers(cust_id) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY (prod_id) REFERENCES products (prod_id) ON DELETE CASCADE ON UPDATE CASCADE) 
"""

#d = """INSERT INTO customers (cust_id, f_name, l_name, email, phone) VALUES (0, "dee", "shish", "deeshish@gmail.com", "+254717018610")"""
"""try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database = "ecommerce_store"
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(customers)
        with connection.cursor() as cursor:
            cursor.execute(d)
            connection.commit()
except Error as e:
    print(e)
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home/")
def home(f_name, l_name):
   try:
        with connect(
                host="localhost",
                user=input("Enter username: "),
                password=getpass("Enter password: "),
                database = 'ecommerce_store'
                ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(customers)
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO customers (f_name, l_name) VALUES ('Mary', 'Okumbe')""")
                connection.commit()
   except Error as e:
       print(e)
   return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("About.html")

@app.route("/gallery/")
def gallery():
    return render_template("Gallery.html")

if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

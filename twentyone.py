from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="address_book"
)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for adding a record
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']
    cursor = mydb.cursor()
    sql = "INSERT INTO contacts (name, address, phone, email) VALUES (%s, %s, %s, %s)"
    val = (name, address, phone, email)
    cursor.execute(sql, val)
    mydb.commit()
    return redirect(url_for('home'))

# Route for modifying a record
@app.route('/modify', methods=['POST'])
def modify():
    search_name = request.form['search_name']
    field = request.form['field']
    value = request.form['value']
    cursor = mydb.cursor()
    sql = "UPDATE contacts SET {} = %s WHERE name = %s".format(field)
    val = (value, search_name)
    cursor.execute(sql, val)
    mydb.commit()
    return redirect(url_for('home'))

# Route for displaying a record
@app.route('/display', methods=['POST'])
def display():
    search_name = request.form['search_name']
    cursor = mydb.cursor()
    sql = "SELECT * FROM contacts WHERE name = %s"
    val = (search_name,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    return render_template('display.html', contact=result)

# Route for deleting a record
@app.route('/delete', methods=['POST'])
def delete():
    search_name = request.form['search_name']
    cursor = mydb.cursor()
    sql = "DELETE FROM contacts WHERE name = %s"
    val = (search_name,)
    cursor.execute(sql, val)
    mydb.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

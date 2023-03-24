from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        event_location = request.form['event_location']
        
        conn = sqlite3.connect('event.db')
        c = conn.cursor()
        c.execute("INSERT INTO registrations (name, email, phone, event_name, event_date, event_location) VALUES (?, ?, ?, ?, ?, ?)", (name, email, phone, event_name, event_date, event_location))
        conn.commit()
        conn.close()
        
        return redirect('/view')
    
    return render_template('register.html')

@app.route('/cancel', methods=['GET', 'POST'])
def cancel():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        event_location = request.form['event_location']
        
        conn = sqlite3.connect('event.db')
        c = conn.cursor()
        c.execute("DELETE FROM registrations WHERE name=? AND email=? AND phone=? AND event_name=? AND event_date=? AND event_location=?", (name, email, phone, event_name, event_date, event_location))
        conn.commit()
        conn.close()
        
        return redirect('/view')
    
    return render_template('cancel.html')

@app.route('/view')
def view():
    conn = sqlite3.connect('event.db')
    c = conn.cursor()
    c.execute("SELECT * FROM registrations")
    rows = c.fetchall()
    conn.close()
    
    return render_template('view.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)

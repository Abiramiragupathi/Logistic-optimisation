from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    with sqlite3.connect('consent.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS consent (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                consent BOOLEAN NOT NULL
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    consent = 'consent' in request.form

    with sqlite3.connect('consent.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO consent (name, email, consent)
            VALUES (?, ?, ?)
        ''', (name, email, consent))
        conn.commit()

    return 'Form submitted successfully!'

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

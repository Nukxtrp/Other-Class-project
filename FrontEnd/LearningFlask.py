from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = "Nukxtrp"

def init_sqlite_db():
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

init_sqlite_db()

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        Username = request.form['username']
        Password = request.form['password']

        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (Username, Password))
        user = c.fetchone()
        conn.close()

        if user:
            session['username'] = Username
            flash("Login successful!")
            return redirect(url_for("home"))
        else:
            flash("Incorrect username or password. Please try again.")
            return render_template("login.html")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        Username = request.form['username']
        Password = request.form['password']
        Correct_Pass = request.form['password_verify']

        if Password != Correct_Pass:
            flash("Passwords do not match!")
            return redirect(url_for('register'))

        try:
            conn = sqlite3.connect('user_database.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (Username, Password))
            conn.commit()
            conn.close()
            flash("Registration successful! Please log in.")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists. Please choose a different one.")
            return redirect(url_for('register'))

    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)

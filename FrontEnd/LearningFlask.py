from flask import Flask, render_template,request

app = Flask(__name__)
app.secret_key = "Nukxtrp"

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Handle login logic here
        pass
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)

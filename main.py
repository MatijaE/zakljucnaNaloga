from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

#app = Flask(__name__)
#app.secret_key = "ključčč"

USERS_FILE = "users.json"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as file:
        return json.load(file)

def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["username"] = username
            session["is_admin"] = True
            return redirect(url_for("admin_dashboard"))
        
        users = load_users()
        user = users.get(username)

        if user and user["password"] == password:
            session["username"] = username
            session["is_admin"] = False
            return redirect(url_for("user_dashboard"))
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        users = load_users()

        if username in users:
            return render_template("register.html", error="Username already exists")
        
        users[username] = {"email": email, "password": password}
        save_users(users)
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/admin")
def admin_dashboard():
    if not session.get("is_admin"):
        return redirect(url_for("login"))

    users = load_users()
    return render_template("admin_dashboard.html", users=users)

@app.route("/dashboard")
def user_dashboard():
    if "username" not in session or session.get("is_admin"):
        return redirect(url_for("login"))
    
    return render_template("user_dashboard.html", username=session["username"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
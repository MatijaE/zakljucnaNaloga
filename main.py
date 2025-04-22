from flask import Flask, render_template, request, redirect, url_for, session
from tinydb import TinyDB, Query
import os

app = Flask(__name__)
app.secret_key = "123"

db = TinyDB("users.json")
User = Query()

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

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

        user = db.get(User.username == username)
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

        if db.get(User.username == username):
            return render_template("register.html", error="Username already exists")

        db.insert({"username": username, "email": email, "password": password})
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/admin")
def admin_dashboard():
    if not session.get("is_admin"):
        return redirect(url_for("login"))

    users = db.all()
    return render_template("admin_dashboard.html", users={u['username']: u for u in users})

@app.route("/delete_user/<username>")
def delete_user(username):
    if not session.get("is_admin"):
        return redirect(url_for("login"))

    db.remove(User.username == username)
    return redirect(url_for("admin_dashboard"))

@app.route("/dashboard")
def user_dashboard():
    if "username" not in session or session.get("is_admin"):
        return redirect(url_for("login"))

    return render_template("user_dashboard.html", username=session["username"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

#za profil
@app.route("/profile")
def profile():
    if "username" not in session:
        return redirect(url_for("login"))

    user = db.get(User.username == session["username"])
    
    #generiranje websita glede na email
    if user and "email" in user:
        email_prefix = user["email"].split("@")[0]
        user["website"] = f"https://livecard.app/{email_prefix}"

    return render_template("profile.html", user=user)

@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        new_data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "bio": request.form["bio"],
            "address": request.form["address"],
            "profile_picture": request.form["profile_picture"],
            "instagram": request.form["instagram"],
            "x": request.form["x"],
            "facebook": request.form["facebook"]
        }
        db.update(new_data, User.username == session["username"])
        return redirect(url_for("profile"))

    user = db.get(User.username == session["username"])
    return render_template("edit_profile.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)
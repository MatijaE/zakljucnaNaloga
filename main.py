from flask import Flask, render_template, request, redirect, url_for, session
from tinydb import TinyDB, Query
from tinyrecord import transaction  #za varno uporabo baze če več uporabnikov hkrati uporablja aplikacijo
import os
import secrets
import bcrypt  #za hashiranje gesel da so varni

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  #za varnost seje

db = TinyDB("users.json")  #tukaj shranjujem uporabnike
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

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:  #če je admin
            session["username"] = username
            session["is_admin"] = True  #nastavim da je admin
            return redirect(url_for("admin_dashboard"))

        user = db.get(User.username == username)  #poišem uporabnika v bazi

        if user and bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):  #preverim geslo
            session["username"] = username
            session["is_admin"] = False  #nastavm da je navaden uporabnik
            return redirect(url_for("user_dashboard"))
        else:
            return render_template("login.html", error="Invalid username or password")  #če so napačni podatki

    return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if db.get(User.username == username):  #če že obstaja uporabnik
            return render_template("register.html", error="Username already exists")  #obvestim uporabnika

        hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())  #hashiram geslo

        with transaction(db) as tr:  #dodam uporabnika v bazo varno če več ljudi hkrati registrira
            tr.insert({
                "username": username,
                "email": email,
                "password": hashed_pw.decode("utf-8")  #bcrypt hash more biti string
            })

        return redirect(url_for("login"))  #po registraciji gre nazaj na prijavo
    return render_template("register.html")

@app.route("/admin")
def admin_dashboard():
    if not session.get("is_admin"):  #če ni admin
        return redirect(url_for("login"))

    users = db.all()  #dobim vse uporabnike
    return render_template("admin_dashboard.html", users={u['username']: u for u in users})  #prikažem uporabnike

@app.route("/delete_user/<username>")
def delete_user(username):
    if not session.get("is_admin"):  #če ni admin
        return redirect(url_for("login"))

    with transaction(db) as tr:  #uporabim transakcijo da se uporabnik varno izbriše
        tr.remove(User.username == username)

    return redirect(url_for("admin_dashboard"))  #nazaj na admin stran

@app.route("/reset_password/<username>")
def reset_password(username):
    if not session.get("is_admin"):  #če ni admin
        return redirect(url_for("login"))

    new_password = "pozablivc"  #novo geslo k ga nastavi admin
    hashed_pw = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt())  #hashiram novo geslo

    with transaction(db) as tr:  #uporabim varno transakcijo
        tr.update({"password": hashed_pw.decode("utf-8")}, User.username == username)  #posodobim geslo

    return redirect(url_for("admin_dashboard"))  #nazaj na admin

@app.route("/dashboard")
def user_dashboard():
    if "username" not in session or session.get("is_admin"):  #če ni loginan ali je admin
        return redirect(url_for("login"))

    return render_template("user_dashboard.html", username=session["username"])  #prikaže uporabnikov dashboard

@app.route("/logout")
def logout():
    session.clear()  #zbriše sejo ob odjavi
    return redirect(url_for("login"))  #po odjavi gre nazaj na prijavo

def generate_website(user):
    if "email" in user and user["email"]:  #če ima uporabnik email
        email_prefix = user["email"].split("@")[0]  #generiram unikatno povezavo
        return f"https://livecard.app/{email_prefix}"
    return None  #če ni emaila vrnem None

@app.route("/profile")
def profile():
    if "username" not in session:  #če ni prijavljen
        return redirect(url_for("login"))

    user = db.get(User.username == session["username"])  #poišem uporabnika v bazi
    if user:
        user["website"] = generate_website(user)  #dodam unikatno povezavo

    return render_template("profile.html", user=user)  #prikažem profil

@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if "username" not in session:  #če ni prijavljen
        return redirect(url_for("login"))

    if request.method == "POST":
        new_data = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "bio": request.form.get("bio"),
            "address": request.form.get("address"),
            "profile_picture": request.form.get("profile_picture"),
            "website": request.form.get("website"),
            "instagram": request.form.get("instagram"),
            "x": request.form.get("x"),
            "facebook": request.form.get("facebook"),
            "whatsapp": request.form.get("whatsapp"),
            "tiktok": request.form.get("tiktok"),
            "snapchat": request.form.get("snapchat"),
            "youtube": request.form.get("youtube"),
            "linkedin": request.form.get("linkedin"),
            "discord": request.form.get("discord")
        }

        with transaction(db) as tr:  #posodobim podatke uporabnika varno če več ljudi ureja profil
            tr.update(new_data, User.username == session["username"])

        return redirect(url_for("profile"))  #nazaj na profil

    user = db.get(User.username == session["username"])  #naložim obstoječe podatke uporabnika
    return render_template("edit_profile.html", user=user)  #prikažem obrazec za urejanje

@app.route("/directory")
def directory():
    if "username" not in session:  #če ni prijavljen
        return redirect(url_for("login"))

    users = db.all()  #dobim vse uporabnike
    for user in users:
        user["website"] = generate_website(user)  #dodam unikatno povezavo vsakemu uporabniku

    return render_template("directory.html", users=users)  #prikažem seznam uporabnikov

if __name__ == "__main__":
    app.run(debug=True)  #zagon v debug načinu
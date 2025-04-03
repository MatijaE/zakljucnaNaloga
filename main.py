from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if User.query.filter_by(email=email).first():
            flash("Uporabnik s tem e-poštnim naslovom že obstaja!", "danger")
            return redirect(url_for("register_user"))

        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registracija uspešna! Sedaj se lahko prijavite.", "success")
        return redirect(url_for("login_user"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password_hash, password):
            flash("Nepravilno uporabniško ime ali geslo.", "danger")
            return redirect(url_for("login_user"))

        login_user(user)
        return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", is_admin=current_user.is_admin)

@app.route("/logout")
@login_required
def logout_user():
    logout_user()
    flash("Uspešno ste se odjavili.", "success")
    return redirect(url_for("login_user"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
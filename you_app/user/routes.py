from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
)
from flask_login import login_user, login_required, logout_user, current_user
from you_app import db
from you_app.models import User

user = Blueprint("user", __name__)


@user.route("/login", methods=["GET", "POST"])
def login():
    """Login user."""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("We couldn't find You! Check your email and try again.")
        elif user and user.verify_password(password):
            login_user(user)
            flash("You have successfully logged in!")
            return redirect(url_for("main.homepage"))
        elif not user.verify_password(password):
            flash("Incorrect password, please try again.")
    return render_template("login.html")


@user.route("/signup", methods=["GET", "POST"])
def register():
    """Register (sign up) new user."""
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        pass_confirm = request.form.get("confirm-password")
        user = User.query.filter_by(email=email).first()
        if user:
            flash(
                """
                A user already exists with that email address.
                Do you need to log in?
                """
            )
        elif password == pass_confirm:
            new_user = User(email=email, username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash("You have successfully signed up! You are now logged in.")
            flash("What can we help You accomplish? Add your goals here!")
            return redirect(url_for("goal.goals"))
    return render_template("register.html")


@user.route("/logout")
@login_required
def logout():
    """Log out user."""
    logout_user()
    flash("You have successfully logged out!")
    return redirect(url_for("main.homepage"))


@user.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    """Allow user to edit their personal settings."""
    if request.method == "GET":
        return render_template("settings.html")
    elif request.method == "POST":
        new_username = request.form.get("username")
        new_email = request.form.get("email")
        new_password = request.form.get("password")
        new_confirm_pass = request.form.get("confirm-password")

        if (
            User.query.filter_by(username=new_username).first()
            and new_username != current_user.username
        ):
            flash("Username taken. Please try again.")
        elif (
            User.query.filter_by(email=new_email).first()
            and new_email != current_user.email
        ):
            flash("An account with that email already exists.")
        elif (
            new_confirm_pass
            and new_password
            and new_confirm_pass == new_password
        ):
            current_user.set_password(new_password)
            db.session.commit()
            flash("Your password has been updated.")
            return redirect(url_for("user.settings"))
        else:
            current_user.username = new_username
            current_user.email = new_email
            db.session.commit()
            flash("Your account has been updated!")
            return redirect(url_for("user.settings"))
        return redirect(url_for("user.settings"))

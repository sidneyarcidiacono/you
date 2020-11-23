from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
)
from flask_login import login_user
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

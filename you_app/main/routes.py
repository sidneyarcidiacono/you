"""Import modules & packages."""
from flask import render_template, Blueprint, request, redirect, url_for
from you_app.models import Challenges, Post, User
from you_app import db

main = Blueprint("main", __name__)


@main.route("/")
def homepage():
    """Show user the homepage."""
    news_feed = Post.query.all()
    return render_template("index.html", news_feed=news_feed)


@main.route("/challenges", methods=["GET", "POST"])
def challenges():
    """Show user available and current challenges."""
    if request.method == "POST":
        title = request.form.get("title")
        dates = request.form.get("dates")
        new_challenge = Challenges(title=title, dates=dates)
        db.session.add(new_challenge)
        db.session.commit()
        return redirect(url_for("main.challenges"))
    new_challenges = Challenges.query.filter_by(completed=False).all()
    completed_challenges = Challenges.query.filter_by(completed=True).all()

    context = {
        "new_challenges": new_challenges,
        "completed_challenges": completed_challenges,
    }
    return render_template("challenges.html", **context)


@main.route("/progress")
def progress():
    """Show user current progress in challenges."""
    return render_template("progress.html")


@main.route("/goals")
def goals():
    """Show user visual representations of their goals."""
    return render_template("goals.html")

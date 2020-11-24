"""Import modules & packages."""
from flask import render_template, Blueprint
from flask_login import current_user
from you_app.models import Post

main = Blueprint("main", __name__)


@main.route("/")
def homepage():
    """Show user the homepage."""
    if current_user.is_authenticated:
        posts = Post.query.all()
        user_challenges = current_user.challenges
        print(f"Current user challenges: {user_challenges}")
        news_feed = posts + user_challenges
        print(f" News feed: {news_feed}")
        return render_template("index.html", news_feed=news_feed)
    else:
        return render_template("index.html")


@main.route("/progress")
def progress():
    """Show user current progress in challenges."""
    return render_template("progress.html")


@main.route("/goals")
def goals():
    """Show user visual representations of their goals."""
    return render_template("goals.html")

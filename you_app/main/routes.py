"""Import modules & packages."""
from flask import render_template, Blueprint
from flask_login import current_user
from you_app.models import Post, Goal

main = Blueprint("main", __name__)


@main.route("/")
def homepage():
    """Show user the homepage."""
    if current_user.is_authenticated:
        posts = Post.query.all()
        user_challenges = current_user.challenges
        news_feed = posts + user_challenges
        goals = Goal.query.filter_by(user_id=current_user.id)
        return render_template("index.html", news_feed=news_feed, goals=goals)
    else:
        return render_template("landing-page.html")

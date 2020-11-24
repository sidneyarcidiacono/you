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
        news_feed = posts + user_challenges
        return render_template("index.html", news_feed=news_feed)
    else:
        return render_template("index.html")

"""Import modules & packages."""
from flask import render_template, Blueprint
from you_app.models import Post

main = Blueprint("main", __name__)


@main.route("/")
def homepage():
    """Show user the homepage."""
    news_feed = Post.query.all()
    return render_template("index.html", news_feed=news_feed)


@main.route("/progress")
def progress():
    """Show user current progress in challenges."""
    return render_template("progress.html")


@main.route("/goals")
def goals():
    """Show user visual representations of their goals."""
    return render_template("goals.html")

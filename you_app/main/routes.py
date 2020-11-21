"""Import modules & packages."""
from flask import render_template, Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def homepage():
    """Show user the homepage."""
    return render_template("index.html")


@main.route("/challenges")
def challenges():
    """Show user available and current challenges."""
    return render_template("challenges.html")


@main.route("/progress")
def progress():
    """Show user current progress in challenges."""
    return render_template("progress.html")


@main.route("/goals")
def goals():
    """Show user visual representations of their goals."""
    return render_template("goals.html")

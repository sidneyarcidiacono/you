"""Package & module import."""
from flask import Blueprint, render_template

progress = Blueprint("progress", __name__)


@progress.route("/progress")
def progress():
    """Show user current progress in challenges."""
    return render_template("progress.html")


# TODO: write routes to pass progress info to front end for rendering graphs

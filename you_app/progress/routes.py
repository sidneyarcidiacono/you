"""Package & module import."""
from flask import Blueprint, render_template
from flask_login import login_required

progress = Blueprint("progress", __name__)


@progress.route("/progress")
@login_required
def progress_page():
    """Show user current progress in challenges."""
    return render_template("progress.html")


# TODO: write routes to pass progress info to front end for rendering graphs

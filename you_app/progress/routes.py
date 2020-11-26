"""Package & module import."""
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from you_app.models import Goal

progress = Blueprint("progress", __name__)


@progress.route("/progress")
@login_required
def progress_page():
    """Show user current progress in challenges."""
    goals = Goal.query.filter_by(user_id=current_user.id)
    return render_template("progress.html", goals=goals)


# TODO: write routes to pass progress info to front end for rendering graphs

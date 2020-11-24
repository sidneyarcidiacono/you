"""Package & module import."""
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

goal = Blueprint("goal", __name__)

# TODO: Routes for users to add goals


@goal.route("/goals")
@login_required
def goals():
    """Show user visual representations of their goals."""
    return render_template("goals.html")


@goal.route("/add_goal", methods=["POST"])
@login_required
def add_goal():
    """Add goal for current_user."""
    pass

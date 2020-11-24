"""Package & module import."""
from flask import Blueprint, render_template

goal = Blueprint("goal", __name__)

# TODO: Routes for users to add goals


@goal.route("/goals")
def goals():
    """Show user visual representations of their goals."""
    return render_template("goals.html")

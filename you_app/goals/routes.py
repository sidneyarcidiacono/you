"""Package & module import."""
from flask import Blueprint, render_template
from flask_login import login_required

goal = Blueprint("goal", __name__)

# TODO: Routes for users to add goals


@goal.route("/goals")
@login_required
def goals():
    """Show user visual representations of their goals."""
    return render_template("goals.html")

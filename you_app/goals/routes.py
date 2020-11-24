"""Package & module import."""
from datetime import datetime
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
from flask_login import login_required, current_user
from you_app.models import Goal
from you_app import db

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
    category = request.form.get("category")
    goal = request.form.get("goal")
    start_date = datetime.strptime(request.form.get("start-date"), "%m-%d-%Y")
    end_date = datetime.strptime(request.form.get("end-date"), "%m-%d-%Y")
    new_goal = Goal(
        category=category,
        goal=goal,
        start_date=start_date,
        end_date=end_date,
        user_id=current_user.id,
    )
    db.session.add(new_goal)
    db.session.commit()
    flash(
        "Great job! You've added a goal! You can add as many as you'd like."
    )
    return redirect(url_for("goal.goals"))

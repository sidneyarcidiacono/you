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
    goals = Goal.query.filter_by(user_id=current_user.id).all()
    for goal in goals:
        goal.daily_expected()
        goal.set_daily_expected_intake()
        db.session.commit()
    return render_template("goals.html", goals=goals)


@goal.route("/add_goal", methods=["POST"])
@login_required
def add_goal():
    """Add goal for current_user."""
    category = request.form.get("category")
    goal = request.form.get("goal")
    start_date = datetime.strptime(request.form.get("start-date"), "%m-%d-%Y")
    end_date = datetime.strptime(request.form.get("end-date"), "%m-%d-%Y")
    baseline = request.form.get("baseline")
    new_goal = Goal(
        category=category,
        goal=goal,
        start_date=start_date,
        end_date=end_date,
        user_baseline=baseline,
        user_id=current_user.id,
    )
    print(f"{new_goal.category}, {new_goal.goal}")
    db.session.add(new_goal)
    db.session.commit()
    flash(
        "Great job! You've added a goal! You can add as many as you'd like."
    )
    return redirect(url_for("goal.goals"))

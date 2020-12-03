"""Package & module import."""
from datetime import datetime
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify,
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
    db.session.add(new_goal)
    db.session.commit()
    flash(
        "Great job! You've added a goal! You can add as many as you'd like."
    )
    return redirect(url_for("goal.goals"))


@goal.route("/edit_goal", methods=["GET", "POST"])
@login_required
def edit_goal():
    """Update user's goal."""
    if request.method == "GET":
        goals = Goal.query.filter_by(user_id=current_user.id).all()
        return render_template("edit_goal.html", goals=goals)
    elif request.method == "POST":
        goal_id = request.form.get("goal-id")
        new_goal_target = request.form.get("goal-target")
        new_start_date = datetime.strptime(
            request.form.get("start-date"), "%m-%d-%Y"
        )
        new_end_date = datetime.strptime(
            request.form.get("end-date"), "%m-%d-%Y"
        )
        goal_to_update = Goal.query.filter_by(id=goal_id).first()
        if new_goal_target != goal_to_update.goal:
            goal_to_update.goal = new_goal_target
        elif new_start_date != goal_to_update.start_date:
            goal_to_update.start_date = new_start_date
        elif new_end_date != goal_to_update.end_date:
            goal_to_update.end_date = new_end_date
        db.session.commit()
        flash("Goal successfully updated!")
        return redirect(url_for("goal.edit_goal"))


@goal.route("/delete_goal", methods=["POST"])
def delete_goal():
    """Delete goal from user goals."""
    goal_id = request.form.get("del-goal-id")
    goal_to_delete = Goal.query.filter_by(id=goal_id).first()
    db.session.delete(goal_to_delete)
    db.session.commit()
    flash("Goal deleted!")
    return redirect(url_for("goal.goals"))

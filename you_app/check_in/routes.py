"""Package & module import."""
from flask import Blueprint, request, redirect, url_for, jsonify
from flask_login import current_user, login_required
from you_app.models import Checkin, Goal
from you_app import db

check_in = Blueprint("check_in", __name__)

# Enable user to check in and add activity/intake for the day


@check_in.route("/add_check_in", methods=["POST"])
@login_required
def add_check_in():
    """Add values for daily goals."""
    category = request.form.get("checkin-category")
    amt_completed = request.form.get("goal")
    for_goal = Goal.query.filter_by(
        user_id=current_user.id, category=category
    ).first()
    for_goal.set_daily_percent_completed(amt_completed)
    check_in = Checkin(
        category=category, amt_completed=amt_completed, goal_id=for_goal.id
    )
    db.session.add(check_in)
    db.session.commit()
    return redirect(url_for("main.homepage"))


@check_in.route("/check_in")
@login_required
def get_goals():
    """Submit goal information for current user to front end."""
    goal_data = {}
    user_goals = Goal.query.filter_by(user_id=current_user.id)
    for goal in user_goals:
        goal_data[goal.id] = goal.category
    return jsonify(goal_data), 200
    if not user_goals:
        return jsonify(
            {
                "msg": """
                        Uh oh, you have to have goals set to check in!
                        Try adding some!
                        """
            }
        )

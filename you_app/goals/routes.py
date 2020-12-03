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


@goal.route("/edit_goal", methods=["POST"])
@login_required
def edit_goal():
    """Update user's goal."""
    goal_to_update = request.form.get("goal_id")
    flash("Goal successfully updated!")
    return redirect(url_for("goal.goals"))


@goal.route("/goal_data", methods=["GET", "POST"])
@login_required
def goal_data():
    """
    Process which goal edit button was clicked.

    Pass back to client.
    """
    goal_id = None
    goal = None
    if request.method == "POST":
        print("We postin")
        goal_id = request.json.get("goalId")
        print(f"Goal id: {goal_id}")
    if request.method == "GET" and goal_id is not None:
        goal = Goal.query.filter_by(id=goal_id)
        print("We gettin")
        data = {
            "goalId": goal.id,
            "goalCategory": goal.category,
            "goalTarget": goal.goal,
        }
        print(f"Data: {data}")
        return jsonify(data), 200
    else:
        print("I never hit an if block")
        return jsonify({"msg": "No goal matches that id"})

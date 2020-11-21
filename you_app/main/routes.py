"""Import modules & packages."""
from flask import render_template, Blueprint
from you_app.models import Challenges
from you_app import db

main = Blueprint("main", __name__)


@main.route("/")
def homepage():
    """Show user the homepage."""
    return render_template("index.html")


@main.route("/challenges")
def challenges():
    """Show user available and current challenges."""
    new_challenge = Challenges(
        title="Test Challenge", dates="June 1, 2020 - July 1, 2020"
    )
    completed_challenge = Challenges(
        title="Finished Challenge",
        dates="May 1, 2020 - May 5, 2020",
        completed=True,
    )
    db.session.add(new_challenge)
    db.session.add(completed_challenge)
    db.session.commit()

    new_challenges = Challenges.query.filter_by(completed=False).all()
    completed_challenges = Challenges.query.filter_by(completed=True).all()

    context = {
        "new_challenges": new_challenges,
        "completed_challenges": completed_challenges,
    }
    return render_template("challenges.html", **context)


@main.route("/progress")
def progress():
    """Show user current progress in challenges."""
    return render_template("progress.html")


@main.route("/goals")
def goals():
    """Show user visual representations of their goals."""
    return render_template("goals.html")

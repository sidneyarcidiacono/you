"""Module & package import."""
from flask import Blueprint, render_template, redirect, url_for, request
from you_app import db
from you_app.models import Challenges
from you_app.main.utils import save_image

challenge = Blueprint("challenge", __name__)


@challenge.route("/challenges", methods=["GET", "POST"])
def challenges():
    """Show user available and current challenges."""
    if request.method == "POST":
        title = request.form.get("title")
        dates = request.form.get("dates")
        image_file = save_image(request.files.get("image"), 1024, "assets")
        new_challenge = Challenges(title=title, dates=dates, image=image_file)
        db.session.add(new_challenge)
        db.session.commit()
        return redirect(url_for("main.challenges"))
    new_challenges = Challenges.query.filter_by(completed=False).all()
    completed_challenges = Challenges.query.filter_by(completed=True).all()

    context = {
        "new_challenges": new_challenges,
        "completed_challenges": completed_challenges,
    }
    return render_template("challenges.html", **context)

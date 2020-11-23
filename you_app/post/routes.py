"""Package & module import."""
from flask import Blueprint, redirect, url_for, request, flash
from flask_login import login_required, current_user
from you_app import db
from you_app.models import Post

post = Blueprint("post", __name__)


@post.route("/add_post", methods=["POST"])
@login_required
def add_post():
    """Add new post to render on homepage."""
    status = request.form.get("status")
    new_post = Post(content=status, user_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()
    flash("Successfully added post!")
    return redirect(url_for("main.homepage"))

"""Package & module import."""
from flask import Blueprint

post = Blueprint("post", __name__)


@post.route("/add_post", methods=["POST"])
def add_post():
    """Add new post to render on homepage."""
    pass

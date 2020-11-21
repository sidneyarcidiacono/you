"""Import modules & packages."""
from flask import render_template, Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def homepage():
    """Show user the homepage."""
    return render_template("index.html")

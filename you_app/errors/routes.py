"""Error handling to display custom 404 page."""
from flask import Blueprint, render_template

error = Blueprint("error", __name__)


@error.app_errorhandler(404)
def show_404(err):
    """Show user custom 404 page."""
    return render_template("404.html")

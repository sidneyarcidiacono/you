"""Package & module import."""
from flask import Blueprint

check_in = Blueprint("check_in", __name__)


@check_in.route("/add_check_in")
def add_check_in():
    """Add values for daily goals."""
    pass
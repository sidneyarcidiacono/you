"""Build out database model classes."""
from you_app import db


class Challenges(db.Model):
    """Create class Challenges to represent db object."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    dates = db.Column(db.String(50), nullable=False)

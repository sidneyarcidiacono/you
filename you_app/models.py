"""Build out database model classes."""
from you_app import db, login_manager
from flask_login import UserMixin
from passlib.hash import sha256_crypt


@login_manager.user_loader
def user_loader(user_id):
    """
    Query user from database.

    This is the user_loader func
    for flask_login.
    """
    return User.query.filter_by(id=user_id).first()


class Challenges(db.Model):
    """Create class Challenges to represent db object."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    dates = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Boolean, default=False)


class Post(db.Model):
    """Create class Post for user posts."""

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(30), nullable=True)
    content = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    likes = db.Column(db.Integer, default=0)


class User(db.Model, UserMixin):
    """Create user class for login & user mgmt."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(120), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    posts = db.relationship(
        "Post", cascade="all, delete", backref="user", lazy=True
    )
    avatar = avatar = db.Column(
        db.String(30),
        nullable=False,
        default="default_profile_pic.jpg",
    )

    def set_is_admin(self):
        """Set is_admin to True under a specific condition."""
        if self.email == "sid@sid.com":
            self.is_admin = True

    def set_password(self, password):
        """Set a hashed password for insertion into db."""
        self.password = sha256_crypt.hash(password)

    def verify_password(self, password):
        """Verify hashed password for log in."""
        return sha256_crypt.verify(password, self.password)

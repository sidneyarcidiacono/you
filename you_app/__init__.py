"""Package and module import."""
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from you_app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

login_manager.login_view = "user.login"

from you_app.main.routes import main
from you_app.user.routes import user
from you_app.post.routes import post
from you_app.challenges.routes import challenge
from you_app.goals.routes import goal
from you_app.progress.routes import progress
from you_app.check_in.routes import check_in
from you_app.errors.routes import error

app.register_blueprint(main)
app.register_blueprint(user)
app.register_blueprint(post)
app.register_blueprint(challenge)
app.register_blueprint(goal)
app.register_blueprint(progress)
app.register_blueprint(check_in)
app.register_blueprint(error)

with app.app_context():
    db.create_all()

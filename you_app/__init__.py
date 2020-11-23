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

app.register_blueprint(main)
app.register_blueprint(user)

with app.app_context():
    db.create_all()

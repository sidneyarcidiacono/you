"""Package and module import."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from you_app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from you_app.main.routes import main

app.register_blueprint(main)

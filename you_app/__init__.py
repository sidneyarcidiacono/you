"""Package and module import."""
from flask import Flask
from you_app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from you_app.main.routes import main

app.register_blueprint(main)

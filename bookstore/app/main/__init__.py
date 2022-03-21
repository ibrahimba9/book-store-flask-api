from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from .config import config_envs

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_envs[config_name])
    flask_bcrypt.init_app(app)
    db.init_app(app)
    app.app_context().push()
    db.create_all()
    return app

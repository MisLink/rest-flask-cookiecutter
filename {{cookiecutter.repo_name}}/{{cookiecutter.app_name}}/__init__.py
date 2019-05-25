from flask import Flask

from . import controllers
from . import errors
from . import extensions
from . import models


def create_app():
    app = Flask(__name__)
    app.config.from_object("{{cookiecutter.app_name}}.config")
    errors.init_app(app)
    extensions.init_app(app)
    controllers.init_app(app)
    models.init_app(app)
    return app

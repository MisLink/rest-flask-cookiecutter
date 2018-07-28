from flask import Flask
from . import controllers
from . import extensions
from . import services
from . import models


def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    app.config.from_pyfile("local_config.py", silent=True)  # load local config
    extensions.init_app(app)
    models.init_app(app)
    controllers.init_app(app)
    services.init_app(app)
    return app

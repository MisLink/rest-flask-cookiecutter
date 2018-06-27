from flask import Flask
from .base import Response
from .controllers import register_blueprint
from .extensions import register_extensions


def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.response_class = Response
    app.config.from_object(config)
    app.config.from_pyfile("local_config.cfg", silent=True)  # load local config
    register_blueprint(app)
    register_extensions(app)
    return app

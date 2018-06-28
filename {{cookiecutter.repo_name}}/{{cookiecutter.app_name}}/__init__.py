from flask import Flask
from .controllers import register_blueprints
from .extensions import register_extensions


def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    app.config.from_pyfile("local_config.cfg", silent=True)  # load local config
    register_blueprints(app)
    register_extensions(app)
    return app

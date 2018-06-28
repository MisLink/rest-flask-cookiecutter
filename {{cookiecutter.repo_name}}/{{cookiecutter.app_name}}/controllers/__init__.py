from .api import api


def register_blueprint(app):
    app.register_blueprint(api)

from flask import Flask
from flask import jsonify
from flask import make_response
from werkzeug.exceptions import HTTPException


def init_app(app: Flask) -> None:
    @app.errorhandler(HTTPException)
    def http_exception_handler(e: HTTPException):
        return make_response(
            jsonify({"code": e.code, "description": e.description}), e.code
        )

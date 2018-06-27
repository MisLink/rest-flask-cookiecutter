import time

from flask import Response as FlaskResponse
from flask import jsonify
from flask.views import MethodView as FlaskMethodView
from werkzeug.exceptions import HTTPException


class Response(FlaskResponse):
    default_mimetype = "application/json"

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (FlaskResponse, HTTPException)):
            pass
        else:
            response = {"data": response, "code": 200, "timestamp": time.time()}
            response = jsonify(response)
        return super().force_type(response, environ)


class MethodView(FlaskMethodView):
    pass

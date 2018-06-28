import time

from flask import Response as FlaskResponse
from flask import jsonify
from flask.views import MethodView as FlaskMethodView


class Response(FlaskResponse):
    pass


class MethodView(FlaskMethodView):
    def dispatch_request(self, *args, **kwargs):
        response = super().dispatch_request(*args, **kwargs)
        try:
            json = {"data": response, "code": 200, "timestamp": time.time()}
            response = jsonify(json)
        except Exception:
            pass
        return response

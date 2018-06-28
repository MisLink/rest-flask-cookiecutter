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
            response = jsonify(
                {"data": response, "code": 200, "timestamp": time.time()}
            )
        except Exception:
            pass
        return response

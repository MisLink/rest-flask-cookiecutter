from flask import jsonify
from flask import Response
from flask.views import MethodView as FlaskMethodView


class MethodView(FlaskMethodView):
    def dispatch_request(self, *args, **kwargs):
        response = super().dispatch_request(*args, **kwargs)
        if not isinstance(response, Response):
            response = jsonify(response)
        return response

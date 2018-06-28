from flask import jsonify
from flask.views import MethodView as FlaskMethodView


class MethodView(FlaskMethodView):
    def dispatch_request(self, *args, **kwargs):
        response = super().dispatch_request(*args, **kwargs)
        try:
            response = jsonify(response)
        except Exception:
            pass
        return response

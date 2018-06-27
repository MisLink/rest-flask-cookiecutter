from flask import make_response, jsonify
from ...errors import APIError


def register_hook(bp):
    @bp.errorhandler(APIError)
    def _(e):
        return make_response(jsonify(e.to_dict()), e.code)

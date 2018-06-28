import time
from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


class APIError(HTTPException):
    def __init__(self, description=None, code=None):
        self.description = description
        self.code = code

    def to_dict(self):
        return {
            "code": self.code,
            "description": self.description,
            "timestamp": time.time(),
        }

    def get_response(self, environ=None):
        return make_response(jsonify(self.to_dict()), self.code)


class BadRequest(APIError):
    def __init__(self, description):
        super().__init__(description=description, code=400)

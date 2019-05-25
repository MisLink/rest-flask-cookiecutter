from typing import Optional
import warnings

from flask import Flask
from flask import jsonify
from flask import make_response


class APIError(Exception):
    code: Optional[int] = None

    def __init__(self, description: str = ""):
        self.description = description

    def to_dict(self) -> dict:
        if self.code is None:
            warnings.warn("Not set HTTP code, the default is 400.")
            self.code = 400
        return {"code": self.code, "description": self.description}


class BadRequest(APIError):
    code = 400


def init_app(app: Flask) -> None:
    app.errorhandler(APIError)(lambda e: make_response(jsonify(e.to_dict()), e.code))

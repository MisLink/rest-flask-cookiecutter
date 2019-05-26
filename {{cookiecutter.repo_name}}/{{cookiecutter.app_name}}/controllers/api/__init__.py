from flask import Blueprint

from .status import StatusAPI

api = Blueprint("api", __name__, url_prefix="/api/1.0")

api.add_url_rule("/status", view_func=StatusAPI.as_view("status"))

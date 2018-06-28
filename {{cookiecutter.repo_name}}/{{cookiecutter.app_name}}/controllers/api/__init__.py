from flask import Blueprint
from .status import Status

api = Blueprint("api", __name__, url_prefix="/api/1.0")

api.add_url_rule("/status", endpoint="status", view_func=Status.as_view("status"))

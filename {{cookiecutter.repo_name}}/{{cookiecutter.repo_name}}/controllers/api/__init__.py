from flask import Blueprint
from .status import Status
from .hook import register_hook

api = Blueprint("api", __name__, url_prefix="/api/1.0")

register_hook(api)

api.add_url_rule("/status", endpoint="status", view_func=Status.as_view("status"))

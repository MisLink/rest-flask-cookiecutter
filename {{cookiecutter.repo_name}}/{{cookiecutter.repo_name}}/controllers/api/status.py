from ...base import MethodView


class Status(MethodView):
    def get(self):
        return "running!"

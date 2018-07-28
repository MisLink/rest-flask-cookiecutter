from {{cookiecutter.app_name}}.base import MethodView


class Status(MethodView):
    def get(self):
        return "running!"

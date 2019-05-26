from {{cookiecutter.app_name}}.base import MethodView


class StatusAPI(MethodView):
    def get(self):
        return "running!"

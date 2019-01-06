from celery import Celery as _Celery, _state


class Celery(_Celery):
    def __init__(self, app=None):
        self._original_register_app = _state._register_app
        _state._register_app = lambda _: None
        super().__init__()
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        _state._register_app = self._original_register_app
        TaskBase = self.Task

        class ContextTask(TaskBase):
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return self.run(*args, **kwargs)

        super().__init__(app.import_name, broker=app.config["CELERY_BROKER_URL"])
        self.conf.update(app.config)
        self.Task = ContextTask

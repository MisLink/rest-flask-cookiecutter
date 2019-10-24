from celery import Task
from flask import Flask

from . import tasks
from .celery import celery

__all__ = ["tasks"]


def init_app(app: Flask):
    celery.main = app.import_name
    celery.config_from_object(app.config, namespace="CELERY")

    class ContextTask(Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    app.extensions["celery"] = celery

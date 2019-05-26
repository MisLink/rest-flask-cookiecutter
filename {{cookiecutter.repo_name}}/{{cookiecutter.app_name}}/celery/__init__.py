from celery import Celery
from celery import Task
from flask import Flask

celery = Celery()


def init_app(app: Flask):
    celery.main = app.import_name
    celery.conf.update(app.config.get_namespace("CELERY_"))

    class ContextTask(Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    app.extensions["celery"] = celery

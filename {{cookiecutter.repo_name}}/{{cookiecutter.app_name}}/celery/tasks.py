from flask import current_app

from . import celery


@celery.task
def func():
    return

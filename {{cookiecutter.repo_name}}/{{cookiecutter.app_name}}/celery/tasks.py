from . import celery


@celery.task
def func():
    return

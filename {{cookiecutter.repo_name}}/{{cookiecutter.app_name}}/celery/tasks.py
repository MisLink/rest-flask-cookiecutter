from .celery import celery


@celery.task
def func():
    return

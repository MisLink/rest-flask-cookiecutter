from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
{% if cookiecutter.task_queue == "celery" -%}
from flask_celery import Celery
{%- endif %}

db = SQLAlchemy()
migrate = Migrate()
{% if cookiecutter.task_queue == "celery" -%}
celery = Celery()
{%- endif %}


def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
    {% if cookiecutter.task_queue == "celery" -%}
    celery.init_app(app)
    {%- endif %}

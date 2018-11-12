import os
from flask.cli import load_dotenv
from {{cookiecutter.app_name}} import create_app
from {{cookiecutter.app_name}}.config import configs

load_dotenv()
app = create_app(configs[os.getenv("FLASK_ENV") or "dev"])

{% if cookiecutter.task_queue == "celery" -%}
from {{cookiecutter.app_name}}.extensions import celery  # noqa
{%- endif %}

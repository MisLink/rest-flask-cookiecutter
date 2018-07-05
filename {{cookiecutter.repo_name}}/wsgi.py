import os

from {{cookiecutter.app_name}} import create_app
from {{cookiecutter.app_name}}.config import configs

app = create_app(configs[os.getenv("FLASK_ENV") or "dev"])

import os

from {{cookiecutter.repo_name}} import create_app
from {{cookiecutter.repo_name}}.config import configs

app = create_app(configs[os.getenv("FLASK_ENV") or "dev"])

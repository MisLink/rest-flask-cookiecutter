class Config:
    SECRET_KEY = "python -c 'import os; print(os.urandom(16))'"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    {% if cookiecutter.task_queue == "celery" -%}
    CELERY_BROKER_URL = ""
    CELERY_INCLUDE = ["{{cookiecutter.app_name}}.tasks"]
    {%- endif %}


class DevConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    pass


configs = {"dev": DevConfig, "prod": ProdConfig, "test": TestConfig}

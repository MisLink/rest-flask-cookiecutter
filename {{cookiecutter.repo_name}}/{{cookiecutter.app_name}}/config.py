class Config:
    SECRET_KEY = "python -c 'import os; print(os.urandom(16))'"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    pass


class PreConfig(ProdConfig):
    pass


configs = {"dev": DevConfig, "pre": PreConfig, "prod": ProdConfig, "test": TestConfig}

class Config:
    SECRET_KEY = b"5X\xbd\xec\xddcL\xa9\x19\xe6\x81\x86\x833\xa9\xfa"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class PreConfig(ProdConfig):
    pass


configs = {"dev": DevConfig, "pre": PreConfig, "prod": ProdConfig, "test": TestConfig}

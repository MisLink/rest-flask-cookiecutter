import os

from flask.cli import load_dotenv

load_dotenv()
# Baisc
ENV = os.getenv("FLASK_ENV") or "dev"
TESTING = True if ENV == "test" else False
SECRET_KEY = os.getenv("SECRET_KEY")

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False

from {{cookiecutter.app_name}} import create_app

app = create_app()

celery = app.extensions["celery"]

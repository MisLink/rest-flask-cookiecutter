import shutil
from pathlib import Path

app_dir = Path("{{cookiecutter.app_name}}")


def remove(path: Path):
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(str(path))


task_queue = "{{cookiecutter.task_queue}}"

if task_queue != "celery":
    remove(Path("flask_celery.py"))
    remove(app_dir / "tasks")

from core.celery import app
from .models import CustomUserProfile


@app.task
def add():
    x = 5
    y = 6
    return x * y


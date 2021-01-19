import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'check-login-every-1-hour': {
        'task': 'app.tasks.check_date',
        'schedule': crontab(minute=0, hour='*/1'),
    },
}
app.conf.timezone = 'Europe/Moscow'

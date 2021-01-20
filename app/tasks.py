from core.celery import app

from django.core.mail import send_mail

from datetime import timedelta, datetime
from django.utils import timezone

from .models import rabotay


@app.task
def check_date():
    date = rabotay.objects.all()
    past = timezone.now() - timedelta(days=1)
    for some_object in date:
        if past > some_object.last_login:
            send_mail(
                'Уважаемый пользователь.',
                'Ваша сессия истекла. Перезайдите на сайт.',
                'privetikgoo11232@gmail.com',
                [some_object.email],
                fail_silently=False,
            )
        else:
            pass



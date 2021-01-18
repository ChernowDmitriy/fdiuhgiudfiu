from core.celery import app

from django.core.mail import send_mail

from time import sleep


@app.task
def send_email_task():
    send_mail(
        'Subject here',
        'Here is the message.',
        'olegkoshelev20005@mail.ru',
        ['olegkoshelev20005@mail.ru'],
        fail_silently=False,
    )
    return None
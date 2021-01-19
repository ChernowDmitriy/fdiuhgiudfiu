from django.shortcuts import render
from django.http import HttpResponse

from .tasks import check_date


def index(request):
    check_date.delay()
    return HttpResponse('<h1>CELERY!!!</h1>')
from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'company_count_application.settings')         #need to Add here project setting

app = Celery('company_count_application')                #need to django project name
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

#Celery Beat Settings
app.conf.beat_schedule={

}


app.autodiscover_tasks()

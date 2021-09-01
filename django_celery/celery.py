from __future__ import absolute_import,unicode_literals
from datetime import timezone

import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery.settings')

app= Celery('django_celery')
app.conf.enable_utc = False
app.conf.update(timezone= 'Asia/Kolkata')
app.config_from_object(settings,namespace='CELERY')

#CELERY SEAT SETTING

app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')

    
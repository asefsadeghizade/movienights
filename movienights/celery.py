import os 

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movienights.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")

import configurations

configurations.setup()

app = Celery("movienights")
app.config_from_object("django.conf.settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
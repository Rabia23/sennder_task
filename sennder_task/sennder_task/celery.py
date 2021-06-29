"""Celery file."""
from __future__ import absolute_import

import os
from datetime import timedelta

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sennder_task.settings")
app = Celery("sennder_task")

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = "django_celery_beat.schedulers.DatabaseScheduler"

app.conf.beat_schedule = {
    "update_db": {
        "task": "apps.api.tasks.update_db",
        "schedule": timedelta(minutes=1),
    },
}

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('hg')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.broker_url = 'redis://redis:6379/0'
app.conf.beat_scheduler = "django_celery_beat.schedulers.DatabaseScheduler"

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    pass

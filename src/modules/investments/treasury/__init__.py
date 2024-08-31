from celery.schedules import crontab
from core.jobs import celery_app

@celery_app.on_after_configure.connect
def setup_sync_treasury_tasks(sender, **kwargs):
    from .tasks import sync_treasury
    sync_treasury.apply_async(countdown=2)

    sender.add_periodic_task(
        crontab(minute='*/30'),
        sync_treasury.s()
    )

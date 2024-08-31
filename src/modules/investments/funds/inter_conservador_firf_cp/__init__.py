from celery.schedules import crontab
from core.jobs import celery_app
from .strategy import InterConservadorFIRFCPStrategy

__all__ = ['InterConservadorFIRFCPStrategy']

@celery_app.on_after_configure.connect
def setup_sync_inter_conservador_firf_cp_tasks(sender, **kwargs):
    from .tasks import sync_inter_conservador_firf_cp
    sync_inter_conservador_firf_cp.apply_async(countdown=10)

    sender.add_periodic_task(
        crontab(minute='0', hour='0'),
        sync_inter_conservador_firf_cp.s()
    )

from django.apps import AppConfig


class TreasuryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.investments.treasury'

    def ready(self) -> None:
        from .tasks import sync_treasury

        sync_treasury.delay()

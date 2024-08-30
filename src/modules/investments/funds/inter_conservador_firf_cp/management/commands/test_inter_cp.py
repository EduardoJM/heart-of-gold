from datetime import date
from django.core.management.base import BaseCommand
from modules.investments.funds.inter_conservador_firf_cp.strategy import InterConservadorFIRFCPStrategy

class Command(BaseCommand):
    def handle(self, *args, **options):
        sttg = InterConservadorFIRFCPStrategy(500, date(2024, 7, 18))
        sttg.compute_value()

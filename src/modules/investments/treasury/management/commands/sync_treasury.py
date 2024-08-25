from django.core.management.base import BaseCommand
from modules.investments.treasury.integration import get_treasury_data
from modules.investments.treasury.models import TreasuryBondInformation

class Command(BaseCommand):
    def handle(self, *args, **options):
        data = get_treasury_data()

        items = data.response.TrsrBdTradgList
        for item in items:
            name = item.TrsrBd.nm
            description = item.TrsrBd.featrs
            unit_price = item.TrsrBd.untrRedVal

            TreasuryBondInformation.objects.update_or_create(
                name=name,
                defaults={'unit_price': unit_price, 'description': description},
            )

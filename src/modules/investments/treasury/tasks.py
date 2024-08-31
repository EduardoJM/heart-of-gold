from celery import shared_task

@shared_task(name='sync_treasury')
def sync_treasury():
    from .integration import get_treasury_data
    from .models import TreasuryBondInformation

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

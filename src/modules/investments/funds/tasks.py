from celery import shared_task

@shared_task(name='compute_fund_value')
def compute_fund_value(fund_pk):
    from .models import Fund
    from .registry import registry

    fund = Fund.objects.get(pk=fund_pk)
    name = fund.name

    strategy_class = registry.get(name)
    strategy = strategy_class(fund.buy_value, fund.buy_date)
    value = strategy.compute_value()

    fund.currently_value = value
    fund.save()

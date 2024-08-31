from celery import shared_task

@shared_task(name="sync_inter_conservador_firf_cp")
def sync_inter_conservador_firf_cp():
    from .integration import get_inter_conservador_firf_cp_data
    from .models import CumulativeReturn

    data = get_inter_conservador_firf_cp_data()
    chart = data.result.pageContext.charts.cumulativeReturn
    fund_line = list(filter(lambda line: line.name == 'Fundo', chart.lines))
    if not fund_line:
        return
    fund_line = fund_line[0]

    for axis in fund_line.data:
        CumulativeReturn.objects.update_from_integration_axis(axis)




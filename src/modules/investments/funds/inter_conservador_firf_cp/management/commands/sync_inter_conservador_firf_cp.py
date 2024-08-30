from django.core.management.base import BaseCommand
from modules.investments.funds.inter_conservador_firf_cp.integration import get_inter_conservador_firf_cp_data
from modules.investments.funds.inter_conservador_firf_cp.models import CumulativeReturn

class Command(BaseCommand):
    def handle(self, *args, **options):
        data = get_inter_conservador_firf_cp_data()

        chart = data.result.pageContext.charts.cumulativeReturn
        fund_line = list(filter(lambda line: line.name == 'Fundo', chart.lines))
        if not fund_line:
            return
        fund_line = fund_line[0]

        for axis in fund_line.data:
            CumulativeReturn.objects.update_from_integration_axis(axis)


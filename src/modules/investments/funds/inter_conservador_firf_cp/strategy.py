from datetime import date
from modules.investments.funds.base import FundStrategyBase, FundComputeMode
from .models import CumulativeReturn

class InterConservadorFIRFCPStrategy(FundStrategyBase):
    fund_name = 'Inter Conservador FIRF CP'
    computation_mode = FundComputeMode.EveryDay
    limit_lose_days = 100

    def compute_value(self):
        now = date.today()

        initial_cumulative = CumulativeReturn.objects.find_nearest_up_date(self.initial_date)
        final_cumulative = CumulativeReturn.objects.find_nearest_down_date(now)
        if not initial_cumulative:
            return self.initial_value

        if not final_cumulative:
            return self.initial_value
        
        diff = final_cumulative.cumulated_return - initial_cumulative.cumulated_return
        return self.initial_value * (1 + diff / 100)

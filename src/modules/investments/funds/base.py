from decimal import Decimal
from enum import Enum
from datetime import date

class FundComputeMode(Enum):
    EveryDay = 'EveryDay'
    EveryHour = 'EveryHour'

class FundStrategyBase:
    computation_mode: FundComputeMode = FundComputeMode.EveryDay
    fund_name: str = ''

    def __init__(self, initial_value: Decimal | float, initial_date: date):
        self.initial_value = initial_value
        self.initial_date = initial_date

    def compute_value(self):
        raise NotImplementedError("compute_value is not implemented yet.")

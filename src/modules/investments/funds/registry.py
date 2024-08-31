from typing import Type
from .base import FundStrategyBase

class FundsRegistry:
    _registry = {}

    def __init__(self):
        self._registry = {}

    def register(self, name: str, cls: Type[FundStrategyBase]):
        self._registry[name] = cls
    
    def get(self, name: str) -> Type[FundStrategyBase]:
        return self._registry[name]
    
    def get_names(self) -> list[str]:
        return self._registry.keys()

registry = FundsRegistry()

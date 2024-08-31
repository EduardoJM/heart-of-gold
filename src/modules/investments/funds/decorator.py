from typing import Type
from .base import FundStrategyBase
from .registry import registry

def register(name: str):
    def _wrapper(strategy_base: Type[FundStrategyBase]):
        registry.register(name, strategy_base)
        return strategy_base
    
    return _wrapper

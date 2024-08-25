from .api_data import (
    TreasuryApiResponse,
    TreasuryBound,
    TreasuryBoundInfo,
    TreasuryResponseData,
    parse_json
)
from .scrap import scrap_treasury_data

def get_treasury_data_from_text(text_data: str):
    return parse_json(text_data)

def get_treasury_data():
    text_data = scrap_treasury_data()
    if not text_data:
        raise Exception()
    return get_treasury_data_from_text(text_data)

__all__ = [
    'get_treasury_data_from_text',
    'get_treasury_data',
    'TreasuryApiResponse',
    'TreasuryBound',
    'TreasuryBoundInfo',
    'TreasuryResponseData'
]

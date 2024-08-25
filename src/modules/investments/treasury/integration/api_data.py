import json
from pydantic import BaseModel

class TreasuryBound(BaseModel):
    nm: str
    featrs: str
    untrRedVal: float

class TreasuryBoundInfo(BaseModel):
    TrsrBd: TreasuryBound

class TreasuryResponseData(BaseModel):
    TrsrBdTradgList: list[TreasuryBoundInfo]

class TreasuryApiResponse(BaseModel):
    responseStatus: int
    response: TreasuryResponseData

def parse_json(data: str):
    json_data = json.loads(data)
    return TreasuryApiResponse(**json_data)

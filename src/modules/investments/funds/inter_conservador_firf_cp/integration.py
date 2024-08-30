from pydantic import BaseModel
import requests

class CumulativeReturnChartLineItem(BaseModel):
    xAxis: str
    yAxis: str

class CumulativeReturnChartLine(BaseModel):
    name: str
    type: str
    data: list[CumulativeReturnChartLineItem]

class CumulativeReturnChart(BaseModel):
    lines: list[CumulativeReturnChartLine]

class Charts(BaseModel):
    cumulativeReturn: CumulativeReturnChart

class PageContext(BaseModel):
    charts: Charts

class Result(BaseModel):
    pageContext: PageContext

class Response(BaseModel):
    result: Result

def get_inter_conservador_firf_cp_data():
    url = 'https://www.interasset.com.br/page-data/fundos-de-credito/inter-conservador-firf-cp/page-data.json'
    response = requests.get(url)
    json_data = response.json()
    return Response(**json_data)

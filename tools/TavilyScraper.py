from crewai.tools import BaseTool
from typing import Type
import requests
from pydantic import BaseModel, Field

TAVILY_CLIENT_API_KEY='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'

class TavilyInput(BaseModel):
    query: str = Field(..., description="Input query for tavily tool")

class TavilyOutput(BaseModel):
    response: str = Field(..., description="Reviews extracted by tavily")


class TavilySearchTool(BaseTool):
    name : str = 'Tavily Search tool'
    description : str = 'Useful to fetch real-time ecommerce data from the web like product prices, reviews, comparisons'
    args_schema : Type[BaseModel] = TavilyInput
    return_schema : Type[BaseModel] = TavilyOutput

    def _run(self, query:str) -> TavilyOutput:
        response = requests.post(
            'https://api.tavily.com/search',
            headers={'Authorization': f"Bearer {TAVILY_CLIENT_API_KEY}"},
            json = {
                'query': query,
                'search_depth': 'advanced',
                'include_answer': True,
                'include_raw_content': False
            }
        )
        data = response.json()
        return TavilyOutput(response=data.get('results', 'No result found'))

    def _arun(self, query: str):
        raise NotImplementedError('Async not implemented')

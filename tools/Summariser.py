from crewai.tools import BaseTool
from typing import Type
from Reviewai.models.LLM import llm
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field


class SummariserInput(BaseModel):
    data: dict = Field(..., description='Sentiment of the user reviews and features of the product')

class SummariserOutput(BaseModel):
    summary : str = Field(..., description='Detailed summary of the product including pros and cons')


class Summariser(BaseTool):
    name : str = "Summary Generating tool"
    description : str = 'Generates a detailed summary for the product from the sentiment analysed for reviews and includes the list of pros/cons'
    args_schema : Type[BaseModel] = SummariserInput
    return_schema : Type[BaseModel] = SummariserOutput

    def _run(self, data) -> SummariserOutput:
        prompt = PromptTemplate.from_template(
            """
                Generates a detailed summary of the product from the data provided:
                {data}
                The data contains the sentiment of the users' reviews and features of the product.
                Along with the summary, generate a list of 
                Pros and Cons
            """
        )
        chain = LLMChain(prompt, llm=llm)
        return SummariserOutput(summary=chain.run(data=data))
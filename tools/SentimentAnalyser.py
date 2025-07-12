from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from Reviewai.models.LLM import llm
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


class SentimentInput(BaseModel):
    review : str = Field(..., description="Users reviews for the product")


class SentimentAnalyser(BaseTool):
    name : str = "Sentiment Analyser and feature extractor tool"
    description : str = "Analyses the sentiment for the reviews and the features extracted from the web"
    args_schema : Type[BaseModel] = SentimentInput

    def _run(self, review) -> dict :
        prompt = PromptTemplate.from_template(
            """Given the following product review:
    
            "{review}"
    
            1. Classify the overall sentiment as Positive, Negative, or Neutral.
            2. Extract product features mentioned and classify their individual sentiment.
    
            Respond in JSON format:
            {
              "overall_sentiment": "...",
              "features": {
                "feature1": "positive",
                "feature2": "negative"
              }
            }
            """
        )
        chain = LLMChain(prompt=prompt, llm=llm)
        return chain.run(review=review)







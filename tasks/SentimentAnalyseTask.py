from crewai import Task
from Reviewai.tools.SentimentAnalyser import SentimentAnalyser
from Reviewai.agents.SentimentAgent import sentiment_agent

sentiment_analyser_and_feature_extractor = SentimentAnalyser()

sentiment_analyse_and_feature_extraction_task = Task(
    description=(
        """
            You are responsible for analyzing the sentiment and extracting features from the list of product reviews.
            You will be given a list of raw customer reviews.
            For each review:
                Determine its sentiment category:
                    - Positive
                    - Moderate
                    - Negative
            Identify and list key product features mentioned.
            For example: battery life, build quality, camera, price, etc.
            Sample Format (for each review):
            {
                "review_text": "The phone lasts long and charges quickly.",
                "sentiment": "Positive",
                "features": ["battery life", "charging speed"]
            }
            ***Output format*** : 
            [
                {
                "review_text": "",
                "sentiment": "",
                "features": []
                },
                {
                "review_text": "",
                "sentiment": "Positive",
                "features": []
                },
                ...
            ]

            Rules:
                - Base your sentiment ONLY on the actual review text — never infer beyond what’s said.
                - Avoid subjective judgments or hallucinations.
                - If a review lacks sentiment or features, mention that explicitly.
            You are a critical gatekeeper for decision-making. Accuracy in sentiment and feature extraction is vital.
        """
    ),
    expected_output="""
        Sentiments and the features of the product.
    """,
    tools=[sentiment_analyser_and_feature_extractor],
    agent=sentiment_agent,
)


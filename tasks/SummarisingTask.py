from crewai import Task
from Reviewai.tools.Summariser import Summariser
from Reviewai.agents.SummariserAgent import summariser_agent


summariser = Summariser()


summarising_task = Task(
    description=(
        """
            You are responsible for creating a concise and informative summary of the product reviews based on prior analysis.
            **Your Input Will Include a list of user reviews**:
            [{
                "review_text": "",
                "sentiment": "",
                "features": []
            },
            {
                "review_text": "",
                "sentiment": "",
                "features": []
            },
            ....
            ]

            ---

            **Your Output Must Include**:
            1. **Overview Summary (3–6 sentences):**
                - Give a balanced overview of how users perceive the product overall.
                - Clearly mention frequently praised features and commonly reported issues.
                - Avoid marketing fluff or exaggeration.

            2. **Pros List (Bullet Points):**
                - Include product features that are mentioned positively in multiple reviews.
                - Use user-relevant terms (e.g., "long battery life" instead of just "battery").
                - Do **not** use vague phrases like "good quality" or "nice design."

            3. **Cons List (Bullet Points):**
                - Highlight features with recurring or critical negative feedback.
                - Be specific, especially for safety issues, technical faults, or unmet expectations.
                - Avoid overgeneralization or adding unsupported criticisms.
            **Rules**:
                - Base your summary only on the input data — do **not fabricate** or assume trends.
                - Stick to real insights derived from user reviews.
                - Your output must help the user make an informed purchase decision with clarity and fairness.
            ***Based on these data, recommend the user whether to buy this product or not.***
            You ensure the user gets a clear, fair snapshot of the product to make a smart purchase decision.
        """
    ),
    expected_output="""
        Overview Summary and the list of Pros and Cons.
    """,
    tools=[summariser],
    agent=summariser_agent,
)

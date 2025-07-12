from crewai import Task
from Reviewai.agents.FetcherAgent import fetcher_agent
from Reviewai.tools.TavilyScraper import TavilySearchTool

tavily_search = TavilySearchTool()

fetching_Task = Task(
    description= (
        """
            You are responsible for collecting genuine customer reviews of the product mentioned in the user query.
            Extract the product name or model explicitly from the query.
            The product query:
                {product_query}
            Do not generate your own reviews.
            Use the tavily_search tool to fetch reviews from credible sources like:
	            - Amazon
	            - Flipkart
	            - Meesho
	            - eBay
	            - Other known ecommerce platforms
            Focus on product-specific user reviews, not generic articles or promotional content.
            Return a cleaned list of reviews, ensuring each review includes:
                - The review text
                - The review source URL
                - If available, review rating (e.g., 4.5/5) and reviewer's name
            **Strict Constraints**:
                Avoid non-review pages like specs, blog posts, or ads.
                Do not summarize or analyze — just fetch the raw review data.
            This task is the first and foundational step of our smart buying assistant. You must ensure data quality and relevance.
        """
    ),
    expected_output="Reviews from known ECommerce sites",
    tools=[tavily_search],
    agent= fetcher_agent,
)
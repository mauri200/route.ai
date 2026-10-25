# tools/search.py
import os
from typing import Literal
from langchain.tools import tool
from tavily import TavilyClient

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

@tool(parse_docstring=True)
def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
) -> dict:
    """Search the internet for relevant trade data, tariffs, harvest seasons, and market demand.

    Args:
        query: The search query.
        max_results: Maximum number of results to return.
        topic: Search topic category.
    """
    return tavily_client.search(query, max_results=max_results, topic=topic)
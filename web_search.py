import requests
from dotenv import load_dotenv
import os
import logging

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
CSE_ID = os.getenv("GOOGLE_CSE_ID")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def search_web(query, num_results=5):
    """Searches the web using Google Custom Search and returns snippets."""
    if not API_KEY or not CSE_ID:
        logger.error("GOOGLE_API_KEY or GOOGLE_CSE_ID is missing. Please set them in your .env file.")
        return ["No evidence found due to missing API keys."]
    try:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {"key": API_KEY, "cx": CSE_ID, "q": query, "num": num_results}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get("items", [])
        snippets = []
        for result in results:
            title = result.get("title", "")
            snippet = result.get("snippet", "")
            snippets.append(f"{title}: {snippet}")
        return snippets
    except Exception as e:
        logger.error(f"[ERROR] Web search failed: {e}")
        return ["No evidence found due to an error."]
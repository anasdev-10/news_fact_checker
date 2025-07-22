import requests
from dotenv import load_dotenv
import os
import logging

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_news():
    """Fetches top US headlines from NewsAPI. Returns a list of articles or an empty list on error."""
    if not NEWS_API_KEY:
        logger.error("NEWS_API_KEY is missing. Please set it in your .env file.")
        raise ValueError("NEWS_API_KEY is missing.")
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get('articles', [])
    except Exception as e:
        logger.error(f"Error fetching news: {e}")
        return []

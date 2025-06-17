import requests
from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")  

def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching news:", response.status_code)
        return []

    data = response.json()
    return data.get('articles', [])

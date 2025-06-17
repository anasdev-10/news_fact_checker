import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
CSE_ID = os.getenv("GOOGLE_CSE_ID")

def search_web(query, num_results=5):
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
        print(f"[ERROR] Web search failed: {e}")
        return ["No evidence found due to an error."]
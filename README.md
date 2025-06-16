# Real-Time News Fact Checker with Manual & Automated Analysis

A Flask-based web app that fetches the latest news, summarizes the content, and performs automated as well as manual fact-checking using Google Gemini API.

## Features

- Fetches latest news from NewsAPI
- Summarizes each article using extractive methods
- Automatically checks factual accuracy using Gemini models
- Allows users to manually enter any claim or article and check its factual correctness
- Displays real-time verdict and supporting evidence

## Setup Instructions

1. Clone this repository:

   ```
   git clone https://github.com/Anas039/news-fact-checker.git
   ```

2. Create a virtual environment and install dependencies:

   ```
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up your API keys:

   - Get your NewsAPI key from https://newsapi.org
   - Get your Gemini API key from https://makersuite.google.com/app/apikey
   - Create a `.env` file or edit your Python files to store them securely

4. Run the app:

   ```
   python app.py
   ```

5. Open `http://127.0.0.1:5000/` in your browser.

## Project Structure

- `app.py` — Main Flask server
- `news_api.py` — Handles news fetching from NewsAPI
- `summarizer.py` — Extracts summaries from articles
- `fact_checker.py` — Integrates Gemini API for fact-checking
- `web_search.py` — Searches the web for supporting evidence
- `templates/index.html` — Frontend interface

## Notes

- Ensure you stay within your Gemini API quota limits.
- For production deployment, secure your API keys and consider moving them to environment variables.





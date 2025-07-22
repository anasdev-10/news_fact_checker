# Real-Time News Fact Checker with Manual & Automated Analysis

A Flask-based web app that fetches the latest news, summarizes the content, and performs automated as well as manual fact-checking using Google Gemini API.

## Features

- Fetches latest news from NewsAPI
- Summarizes each article using extractive methods
- Automatically checks factual accuracy using Gemini models
- Allows users to manually enter any claim or article and check its factual correctness
- Displays real-time verdict and supporting evidence

## Setup Instructions (Local)

1. Clone this repository:

   ```
   git clone https://github.com/Anas039/news_fact_checker.git
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
   - Get your Google Custom Search API key and CSE ID from https://programmablesearchengine.google.com/
   - Create a `.env` file in the `news_fact_checker` directory (see `.env.example` for required variables)

4. Run the app:

   ```
   python app.py
   ```

5. Open `http://127.0.0.1:5000/` in your browser.

## Hugging Face Spaces Deployment

1. **Create a new Space** on [Hugging Face Spaces](https://huggingface.co/spaces) and select the "Flask" SDK.
2. **Upload all project files** (except your real `.env` file) to the Space.
3. **Set your API keys as Secrets** in the Space settings:
   - Go to your Space > Settings > Secrets.
   - Add the following secrets:
     - `NEWS_API_KEY`
     - `GEMINI_API_KEY`
     - `GOOGLE_API_KEY`
     - `GOOGLE_CSE_ID`
     - `FLASK_SECRET_KEY`
   - **Never upload your real `.env` file or API keys to the repository.**
4. **Ensure your `requirements.txt` is up to date** with all dependencies.
5. The Space will automatically run `app.py` as the entry point.

## Project Structure

- `app.py` — Main Flask server
- `news_api.py` — Handles news fetching from NewsAPI
- `summarizer.py` — Extracts summaries from articles
- `fact_checker.py` — Integrates Gemini API for fact-checking
- `web_search.py` — Searches the web for supporting evidence
- `templates/index.html` — Frontend interface

## Notes

- Ensure you stay within your Gemini API quota limits.
- For production deployment, secure your API keys using environment variables or Hugging Face Secrets.
- For local development, use a `.env` file (never commit this file to public repos).





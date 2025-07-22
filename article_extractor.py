from newspaper import Article
import logging

def extract_full_content(url):
    """Extracts and returns the full text content from a news article URL."""
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text.strip()
    except Exception as e:
        logging.error(f"[EXTRACT ERROR] Could not extract from: {url}\nReason: {e}")
        return None

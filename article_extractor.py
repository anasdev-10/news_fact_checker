from newspaper import Article

def extract_full_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text.strip()
    except Exception as e:
        print(f"[EXTRACT ERROR] Could not extract from: {url}\nReason: {e}")
        return None

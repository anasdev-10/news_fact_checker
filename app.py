from flask import Flask, render_template, request, flash
import os
from news_api import fetch_news
from summarizer import summarize_article
from fact_checker import fact_check_article

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev')  

@app.route('/', methods=['GET', 'POST'])
def home():
    """Main route: displays news, handles manual and article-based fact-checking."""
    try:
        articles = fetch_news()
    except Exception as e:
        flash(f"Error fetching news: {e}", "error")
        articles = []
    for article in articles:
        content = article.get('content') or article.get('description') or ''
        summary = summarize_article(content)
        article['summary'] = summary

    fact_verdict = None
    fact_evidence = None

    # Manual input fact-check
    if request.method == 'POST':
        manual_text = request.form.get('manual_text', '').strip()
        if manual_text:
            fact_verdict, fact_evidence = fact_check_article(manual_text)
        elif 'fact_check' in request.form:
            try:
                article_index = int(request.form['fact_check'])
                summary = articles[article_index]['summary']
                fact_verdict, fact_evidence = fact_check_article(summary)
            except (ValueError, IndexError):
                flash("Invalid article selection for fact-checking.", "error")

    return render_template('index.html', articles=articles, fact_verdict=fact_verdict, fact_evidence=fact_evidence)

if __name__ == '__main__':
    """Run the Flask app."""
    app.run(debug=True, host="0.0.0.0", port=5000)


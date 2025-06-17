from flask import Flask, render_template, request 
from news_api import fetch_news
from summarizer import summarize_article
from fact_checker import fact_check_article

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    articles = fetch_news()
    for article in articles:
        content = article.get('content') or article.get('description') or ''
        summary = summarize_article(content)
        article['summary'] = summary

    fact_verdict = None
    fact_evidence = None

    # Manual input fact-check
    if request.method == 'POST':
        if 'manual_text' in request.form and request.form['manual_text'].strip():
            manual_text = request.form['manual_text']
            fact_verdict, fact_evidence = fact_check_article(manual_text)
        elif 'fact_check' in request.form:
            article_index = int(request.form['fact_check'])
            summary = articles[article_index]['summary']
            fact_verdict, fact_evidence = fact_check_article(summary)

    return render_template('index.html', articles=articles, fact_verdict=fact_verdict, fact_evidence=fact_evidence)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port=7860)


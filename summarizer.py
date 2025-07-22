from transformers import pipeline
import logging

# Initialize summarization pipeline 
try:
    summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
except Exception as e:
    summarizer_pipeline = None
    logging.error(f"Failed to load summarization model: {e}")

# Simple cache dictionary
summary_cache = {}

def summarize_article(article_text):
    """Summarizes the given article text using a transformer model."""
    if not article_text or len(article_text.strip()) == 0:
        return "No content to summarize."
    if summarizer_pipeline is None:
        return "Summarization model not available."
    # Check cache first
    if article_text in summary_cache:
        return summary_cache[article_text]
    try:
        # Truncate input to max token limit for the model 
        max_input_length = 1024
        trimmed_text = article_text[:max_input_length]
        # Generate summary
        summary_list = summarizer_pipeline(trimmed_text, max_length=130, min_length=30, do_sample=False)
        summary = summary_list[0]['summary_text']
        # Cache the result
        summary_cache[article_text] = summary
        return summary
    except Exception as e:
        logging.error(f"Error summarizing article: {e}")
        return "Error generating summary."

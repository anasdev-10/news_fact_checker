import google.generativeai as genai
from web_search import search_web
from dotenv import load_dotenv
import os

load_dotenv()

# Configure with your Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY")) 

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def fact_check_article(summary):
    if not summary:
        return "Unclear", "No summary provided."

    # 1. Search the web for supporting content
    search_results = search_web(summary)
    if not search_results:
        return "Unclear", "No relevant evidence found in search results."

    # 2. Combine search results into context
    context = "\n".join(search_results)

    # 3. Build the prompt for Gemini
    prompt = f"""
You are a fact-checking assistant. Based on the article summary and evidence from search results,
determine whether the summary is likely true, false, or unclear.

Article Summary:
\"\"\"
{summary}
\"\"\"

Search Evidence:
\"\"\"
{context}
\"\"\"

Give a final verdict ("Likely True", "Likely False", or "Unclear") and explain why.
"""

    try:
        response = model.generate_content(prompt)
        output = response.text.strip()

        # Basic parsing logic
        verdict = "Unclear"
        if "likely true" in output.lower():
            verdict = "Likely True"
        elif "likely false" in output.lower():
            verdict = "Likely False"

        return verdict, output

    except Exception as e:
        return "Unclear", f"Error: {str(e)}"

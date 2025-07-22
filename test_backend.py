import unittest
from unittest.mock import patch, MagicMock
import news_api
import summarizer
import fact_checker
import web_search

class TestNewsFactCheckerBackend(unittest.TestCase):
    @patch('news_api.requests.get')
    def test_fetch_news_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'articles': [{'title': 'Test'}]}
        articles = news_api.fetch_news()
        self.assertIsInstance(articles, list)
        self.assertEqual(articles[0]['title'], 'Test')

    @patch('news_api.requests.get')
    def test_fetch_news_failure(self, mock_get):
        mock_get.side_effect = Exception('API error')
        articles = news_api.fetch_news()
        self.assertEqual(articles, [])

    def test_summarize_article_empty(self):
        summary = summarizer.summarize_article("")
        self.assertIn("No content", summary)

    @patch('summarizer.summarizer_pipeline')
    def test_summarize_article_success(self, mock_pipeline):
        mock_pipeline.return_value = [{'summary_text': 'Short summary.'}]
        summary = summarizer.summarize_article('Some long article text.')
        self.assertEqual(summary, 'Short summary.')

    @patch('fact_checker.model')
    @patch('fact_checker.search_web')
    def test_fact_check_article_success(self, mock_search_web, mock_model):
        mock_search_web.return_value = ['Evidence snippet.']
        mock_model.generate_content.return_value.text = 'Likely True: This is correct.'
        verdict, output = fact_checker.fact_check_article('Test summary')
        self.assertEqual(verdict, 'Likely True')
        self.assertIn('correct', output.lower())

    @patch('web_search.requests.get')
    def test_search_web_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'items': [{'title': 'Title', 'snippet': 'Snippet'}]
        }
        results = web_search.search_web('query')
        self.assertTrue(any('Title' in r for r in results))

    @patch('web_search.requests.get')
    def test_search_web_failure(self, mock_get):
        mock_get.side_effect = Exception('API error')
        results = web_search.search_web('query')
        self.assertIn('No evidence found', results[0])

if __name__ == '__main__':
    unittest.main() 
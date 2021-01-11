import unittest
from wws import (
    get_wiki_text
)

class TestWikiWordScraper(unittest.TestCase):
    
    def test_get_wiki_text(self):
        result: str = get_wiki_text()
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()

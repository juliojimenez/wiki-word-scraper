import unittest
from wws import (
    get_wiki_text,
    word_list
)

class TestWikiWordScraper(unittest.TestCase):
    
    def test_get_wiki_text(self):
        result: str = get_wiki_text()
        self.assertIsInstance(result, str)

    def test_word_list(self):
        with open("testdata/test.html", "r") as f:
            test_html: str = f.read()
        result: list = word_list(test_html)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)


if __name__ == "__main__":
    unittest.main()

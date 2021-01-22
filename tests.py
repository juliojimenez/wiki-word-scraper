import io
from typing import _SpecialForm
import unittest
from unittest.mock import MagicMock, patch
from wws import add_to_main_file, get_wiki_text, word_list


class TestWikiWordScraper(unittest.TestCase):
    def test_add_to_main_file(self):
        with patch("builtins.open", create=True) as mock_open:
            mock_open.return_value: _SpecialForm = MagicMock(spec=io.IOBase)
            result: bool = add_to_main_file("/some/path", ["a", "b", "c"])
        self.assertTrue(result)

    def test_get_wiki_text(self):
        result: str = get_wiki_text()
        self.assertIsInstance(result, str)

    def test_word_list(self):
        print("[T] Testing with testdata/test.html")
        with open("testdata/test.html", "r") as f:
            test_html: str = f.read()
        result: list = word_list(test_html)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)


if __name__ == "__main__":
    unittest.main()

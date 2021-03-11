import io
from typing import _SpecialForm
import unittest
from unittest.mock import MagicMock, patch
from wws import (
    add_to_main_file,
    get_wiki_text,
    word_list,
    clean_list,
    file_backup,
    clean_write_to_file,
    get_file_size,
    check_word_count,
    max_length,
)


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

    def test_clean_list(self):
        print("[T] Testing with testdata/cleanlist.txt")
        result: list = clean_list("testdata/cleanlist.txt")
        self.assertEqual(result, ["four", "one", "three", "two"])

    @patch("shutil.copyfile")
    @patch("os.unlink")
    def test_file_backup(self, mock_unlink, mock_copyfile):
        result: bool = file_backup("wtf.txt")
        self.assertTrue(result)

    def test_clean_write_to_file(self):
        with patch("builtins.open", create=True) as mock_open:
            mock_open.return_value: _SpecialForm = MagicMock(spec=io.IOBase)
            result: bool = clean_write_to_file("/some/path", ["a", "b", "c"])
        self.assertTrue(result)

    @patch("os.path.getsize")
    def test_get_file_size(self, mock_getsize):
        mock_getsize.return_value = 123456789
        result: bool = get_file_size("some/path")
        self.assertTrue(result)

    def test_check_word_count_true(self):
        words: int = 1
        word_list: list = ["alice", "bob"]
        result: bool = check_word_count(words, word_list)
        self.assertTrue(result)

    def test_check_word_count_false(self):
        words: int = 0
        word_list: list = ["alice", "bob"]
        result: bool = check_word_count(words, word_list)
        self.assertFalse(result)

    def test_max_length(self):
        word_list: list = ["alice", "bob"]
        max_word_length: int = 3
        result: list = max_length(word_list, max_word_length)
        self.assertEquals(result, ["bob"])


if __name__ == "__main__":
    unittest.main()

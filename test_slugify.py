import unittest

from slugify import slugify


class SlugifyTests(unittest.TestCase):
    def test_basic_punctuation_and_space(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_runs_collapse_and_edges_trim(self):
        cases = [
            ("  Multiple   SPACES\tand\npunctuation!!! ", "multiple-spaces-and-punctuation"),
            ("-leading and trailing-", "leading-and-trailing"),
            ("a--b", "a-b"),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(slugify(text), expected)

    def test_empty_and_separator_only_return_empty(self):
        for text in ["", "   ", "!!!", "---"]:
            with self.subTest(text=text):
                self.assertEqual(slugify(text), "")

    def test_non_ascii_is_a_separator(self):
        cases = [
            ("aKb", "a-b"),  # Kelvin sign lowercases to ASCII "k"
            ("K", ""),
            ("Café au lait", "caf-au-lait"),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(slugify(text), expected)

    def test_digits_preserved(self):
        self.assertEqual(slugify("Version 2.0 Release"), "version-2-0-release")


if __name__ == "__main__":
    unittest.main()

import unittest

from app.myregex import pattern


class TestSourceWordMeaningChecker(unittest.TestCase):
    def test_regex(self):
        self.assertEqual('Hello', pattern.match('Hello world').group(0))


if __name__ == '__main__':
    unittest.main()

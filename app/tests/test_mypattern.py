import unittest

from src.mypattern import pattern


class TestPattern(unittest.TestCase):
    def test_regex(self):
        self.assertEqual('Hello', pattern.match('Hello world').group(0))


if __name__ == '__main__': unittest.main()

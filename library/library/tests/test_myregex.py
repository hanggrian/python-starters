import unittest

from library.myregex import REGEX


class TestRegex(unittest.TestCase):
    def test_regex(self):
        self.assertIsNotNone(REGEX)


if __name__ == '__main__':
    unittest.main()

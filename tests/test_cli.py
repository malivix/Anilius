import unittest


class TestCLI(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

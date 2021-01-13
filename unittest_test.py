import unittest


class TestDivision(unittest.TestCase):
    def test1(self):
        self.assertIs(2, 1, msg='fail')


# how to run tests:   python -m unittest unittest_test.py

import unittest
from unittest_python.Calculator import *


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.a = Calculator()

    def test_upper(self):
        self.assertEqual(1+4, 5)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

    def test_calculator_sum_tenplustwenty(self):
        self.assertEqual(30, self.a.my_sum(10,20))

    def test_calculator_divide_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.a.my_divide(10/0)

if __name__ == '__main__':
    unittest.main()



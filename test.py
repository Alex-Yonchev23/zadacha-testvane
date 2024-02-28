# test.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Calculator.add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(Calculator.subtract(5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(Calculator.multiply(2, 4), 8)

    def test_division(self):
        self.assertEqual(Calculator.divide(6, 2), 3)

# test_integration.py

import unittest
from calculator import Calculator
from logger import Logger
import os

class TestIntegration(unittest.TestCase):

    def test_addition_with_logging(self):
        Calculator.add(2, 3)
        log_content = self.read_log_file()
        self.assertIn("2 + 3 = 5", log_content)

    def test_subtraction_with_logging(self):
        Calculator.subtract(5, 2)
        log_content = self.read_log_file()
        self.assertIn("5 - 2 = 3", log_content)

    def test_multiplication_with_logging(self):
        Calculator.multiply(2, 4)
        log_content = self.read_log_file()
        self.assertIn("2 * 4 = 8", log_content)

    def test_division_with_logging(self):
        Calculator.divide(6, 2)
        log_content = self.read_log_file()
        self.assertIn("6 / 2 = 3", log_content)

    def read_log_file(self):
        with open("log.txt", "r") as log_file:
            return log_file.read()

    def tearDown(self):
        if os.path.exists("log.txt"):
            os.remove("log.txt")

if __name__ == "__main__":
    unittest.main()

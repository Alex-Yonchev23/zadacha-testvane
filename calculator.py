# calculator.py
from logger import Logger

class Calculator:
    @staticmethod
    def add(x, y):
        result = x + y
        Logger.log_operation("+", x, y, result)
        return result

    @staticmethod
    def subtract(x, y):
        result = x - y
        Logger.log_operation("-", x, y, result)
        return result

    @staticmethod
    def multiply(x, y):
        result = x * y
        Logger.log_operation("*", x, y, result)
        return result

    @staticmethod
    def divide(x, y):
        if y != 0:
            result = x / y
            Logger.log_operation("/", x, y, result)
            return result
        else:
            raise ValueError("Cannot divide by zero.")

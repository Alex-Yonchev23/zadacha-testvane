# main.py

from calculator import Calculator

def main():
    x = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    y = float(input("Enter second number: "))

    if operation == '+':
        result = Calculator.add(x, y)
    elif operation == '-':
        result = Calculator.subtract(x, y)
    elif operation == '*':
        result = Calculator.multiply(x, y)
    elif operation == '/':
        try:
            result = Calculator.divide(x, y)
        except ValueError as e:
            result = str(e)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()

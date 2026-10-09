# Create separate functions for addition, subtraction, multiplication, and division.
# Pass these functions as arguments to another function called calculate().
# Program: Calculator Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Error"

def calculate(func, a, b):
    return func(a, b)

print(calculate(add, 10, 5))
print(calculate(multiply, 10, 5))

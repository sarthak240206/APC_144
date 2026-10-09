# Write a function factorial(n) that accepts an integer and returns its factorial.
# Program: Factorial

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))

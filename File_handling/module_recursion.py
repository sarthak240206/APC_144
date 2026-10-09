import recursion_utils

num = int(input("Enter a number: "))

print(f"Factorial of {num}:", recursion_utils.factorial(num))
print(f"Fibonacci number at position {num}:", recursion_utils.fibonacci(num))
print(f"Sum of digits of {num}:", recursion_utils.sum_of_digits(num))
print(f"Binary representation of {num}:", recursion_utils.to_binary(num))

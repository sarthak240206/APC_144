# Convert a decimal number into binary using recursion without using Python's built-in conversion functions.
# Program: Decimal to Binary

def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

print(decimal_to_binary(10) or "0")

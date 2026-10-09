# Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
# Program: Is Prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))

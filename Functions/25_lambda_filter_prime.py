# Programs on Lambda Function
# Take a list of integers, use filter() with an appropriate lambda expression to identify prime numbers.
# Program: Lambda Filter Prime

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primes = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1)), numbers))

print(primes)

# Programs on Lambda Function
# Take a list of integers, use filter() and lambda to extract all even numbers.
# Program: Lambda Filter Even

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)

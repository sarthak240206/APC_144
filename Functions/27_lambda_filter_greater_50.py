# Programs on Lambda Function
# Take a list of numbers, use filter() and lambda to find numbers greater than 50.
# Program: Lambda Filter Greater 50

numbers = [10, 45, 60, 23, 89, 34, 56, 78, 90, 11]
greater = list(filter(lambda x: x > 50, numbers))

print(greater)

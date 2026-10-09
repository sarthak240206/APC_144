# Programs on Lambda Function
# Use filter() and lambda to extract positive numbers from a list.
# Program: Lambda Filter Positive

numbers = [-5, 3, -2, 8, -1, 0, 4]
positive = list(filter(lambda x: x > 0, numbers))

print(positive)

# Programs on Lambda Function
# Take a list of numbers, use map() and a lambda function to generate a list containing their squares.
# Program: Lambda Map Squares

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))

print(squares)

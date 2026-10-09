# Programs on Lambda Function
# Take two lists of numbers, use map() and lambda to create a third list containing the sum of corresponding elements.
# Program: Lambda Map Sum

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
result = list(map(lambda a, b: a + b, list1, list2))

print(result)

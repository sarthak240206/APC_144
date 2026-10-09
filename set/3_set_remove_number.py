# Create a set of numbers and remove a specified number from the set.
# Program: Remove Number

numbers = {1, 2, 3, 4, 5}
num = int(input("Enter number to remove: "))
numbers.discard(num)
print(numbers)

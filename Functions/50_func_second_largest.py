# Create a function to find the second-largest number in a list.
# Program: Second Largest

def second_largest(lst):
    lst.sort()
    return lst[-2]

print(second_largest([12, 45, 67, 89, 23]))

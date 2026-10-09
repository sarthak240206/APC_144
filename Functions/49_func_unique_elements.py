# Write a function that accepts a list and returns a new list containing only unique elements.
# Program: Unique Elements

def unique_elements(lst):
    return list(set(lst))

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))

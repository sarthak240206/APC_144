# Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
# Program: Largest Without Max

def largest(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

print(largest([12, 45, 6, 89, 34]))

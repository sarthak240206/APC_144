# Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.
# Program: List Stats

def list_stats(lst):
    return min(lst), max(lst), sum(lst), sum(lst)/len(lst)

print(list_stats([10, 20, 30, 40, 50]))

# Write a recursive function to search for an element in a sorted list using binary search.
# Program: Binary Search

def binary_search(lst, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search(lst, target, mid + 1, high)
    else:
        return binary_search(lst, target, low, mid - 1)

lst = [1, 3, 5, 7, 9, 11]
print(binary_search(lst, 7, 0, len(lst) - 1))

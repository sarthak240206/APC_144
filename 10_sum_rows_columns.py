import numpy as np

matrix = np.array([[2, 4, 6, 8], [1, 3, 5, 7], [10, 20, 30, 40], [5, 10, 15, 20]])

print('Matrix:\n', matrix)
print('\nSum of each row (axis=1):', np.sum(matrix, axis=1))
print('Sum of each column (axis=0):', np.sum(matrix, axis=0))

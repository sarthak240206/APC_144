import numpy as np

matrix = np.arange(1, 17).reshape(4, 4)

print('Original 4x4 Matrix:\n', matrix)
print('\nFirst row:', matrix[0, :])
print('Last column:', matrix[:, -1])
print('Diagonal elements:', np.diagonal(matrix))
print('Elements from 2nd and 3rd rows:\n', matrix[1:3, :])

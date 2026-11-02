import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)
flattened = arr.flatten()

print('Original 3D Array:\n', arr)
print('\nFlattened 1D Array:\n', flattened)

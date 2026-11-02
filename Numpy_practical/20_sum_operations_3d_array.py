import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print('3D Array (2x3x4):\n', arr)
print('\nSum of all elements:', np.sum(arr))
print('Sum of each layer (axis=(1,2)):', np.sum(arr, axis=(1, 2)))
print('Sum along rows (axis=1):\n', np.sum(arr, axis=1))
print('Sum along columns (axis=2):\n', np.sum(arr, axis=2))

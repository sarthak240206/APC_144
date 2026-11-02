import numpy as np

np.random.seed(0)
arr = np.random.randint(1, 100, size=(3, 4, 5))

print('Random 3D Array (3x4x5):\n', arr)
print('\nMean:', np.mean(arr))
print('Median:', np.median(arr))
print('Standard Deviation:', np.std(arr))
print('Variance:', np.var(arr))
print('Minimum:', np.min(arr))
print('Maximum:', np.max(arr))

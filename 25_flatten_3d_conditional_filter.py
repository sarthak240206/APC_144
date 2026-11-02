import numpy as np

np.random.seed(10)
arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()

avg_val = np.mean(flat)

print('Flattened Array:\n', flat)
print('\nAverage value:', avg_val)
print('\nElements greater than 50:\n', flat[flat > 50])
print('\nEven elements:\n', flat[flat % 2 == 0])
print('\nElements less than average value:\n', flat[flat < avg_val])

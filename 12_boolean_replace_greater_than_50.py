import numpy as np

arr = np.array([12, 65, 34, 89, 45, 52, 23, 78, 90, 11])

print('Original Array:', arr)
arr[arr > 50] = 0
print('Modified Array (elements > 50 replaced with 0):', arr)

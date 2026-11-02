import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

h_concat = np.hstack((a, b))
v_concat = np.vstack((a, b))

print('Array A:\n', a)
print('Array B:\n', b)
print('\nHorizontal Concatenation:\n', h_concat)
print('\nVertical Concatenation:\n', v_concat)

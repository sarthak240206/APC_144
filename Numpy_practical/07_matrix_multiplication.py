import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8], [9, 1], [2, 3]])

res = np.matmul(a, b)

print('Matrix A (2x3):\n', a)
print('Matrix B (3x2):\n', b)
print('Matrix Multiplication (A x B):\n', res)

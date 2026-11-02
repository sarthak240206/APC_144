import numpy as np

arr = np.arange(1, 13)

m_2x6 = arr.reshape(2, 6)
m_3x4 = arr.reshape(3, 4)
m_4x3 = arr.reshape(4, 3)

print('Original 1D Array:', arr)
print('\n2x6 Matrix:\n', m_2x6)
print('\n3x4 Matrix:\n', m_3x4)
print('\n4x3 Matrix:\n', m_4x3)

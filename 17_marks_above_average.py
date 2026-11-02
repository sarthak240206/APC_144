import numpy as np

marks = np.array([55, 62, 78, 84, 91, 45, 68, 72, 80, 89, 65, 74, 82, 90, 71, 60, 77, 85, 93, 69])

avg = np.mean(marks)
above_avg = marks[marks > avg]

print('Total 20 Student Marks:', marks)
print('Class Average:', avg)
print('Marks above Class Average:', above_avg)

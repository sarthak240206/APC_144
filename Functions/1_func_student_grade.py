# Create a function that accepts marks in five subjects and returns the student's percentage and grade.
# Program: Student Grade

def student_result(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 75:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    else:
        grade = 'D'
    return percentage, grade

p, g = student_result(85, 90, 78, 92, 88)
print(f"Percentage: {p}, Grade: {g}")

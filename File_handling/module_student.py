import student

marks = [85, 90, 78, 88, 92]
total = student.calculate_total(marks)
pct = student.calculate_percentage(marks)
grade = student.calculate_grade(pct)

print("Marks:", marks)
print("Total Marks:", total)
print("Percentage:", f"{pct:.2f}%")
print("Grade:", grade)

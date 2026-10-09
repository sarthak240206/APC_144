from student.marks import calculate_total, calculate_percentage
from student.grade import calculate_grade
from student.attendance import check_eligibility

student_name = "Priya Sharma"
marks = [85, 92, 78, 88, 90]
attended = 42
total_classes = 50

total = calculate_total(marks)
pct = calculate_percentage(marks)
grade = calculate_grade(pct)
eligible, att_pct = check_eligibility(attended, total_classes)

print("Student Name:", student_name)
print("Total Marks:", total)
print("Percentage:", f"{pct:.2f}%")
print("Grade:", grade)
print(f"Attendance: {att_pct:.2f}%")
print("Exam Eligibility:", "Eligible" if eligible else "Not Eligible")

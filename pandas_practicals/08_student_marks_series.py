import pandas as pd

marks = pd.Series({"Asha": 85, "Rahul": 72, "Neha": 90, "Amit": 65, "Priya": 78})
print("Student marks:\\n", marks)
student = input("Enter student name to look up: ")
if student in marks:
    print(student, "scored", marks[student])
else:
    print("Student not found")
print("Maximum marks:", marks.max())
print("Minimum marks:", marks.min())
print("Average marks:", marks.mean())
print("Students scoring above 75:\\n", marks[marks > 75])

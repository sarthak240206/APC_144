students = {
    "Rahul": 85,
    "Amit": 92,
    "Sneha": 78,
    "Priya": 95,
    "Neha": 88
}

highest_student = max(students, key=students.get)

print("Student with highest marks:", highest_student)
print("Highest marks:", students[highest_student])

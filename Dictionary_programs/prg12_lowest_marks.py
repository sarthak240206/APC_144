# Create a dictionary containing student names and marks. Find the student with the lowest marks.

students = {
    "Amit": 85,
    "Priya": 90,
    "Rahul": 78
}
low = min(students, key=students.get)
print("Lowest:", low, students[low])

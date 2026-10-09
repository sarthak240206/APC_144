# Programs on Lambda Function
# Take a list containing student names and marks, use functions and lambda expressions to:
# Calculate average marks. Filter students scoring above 75. Sort students according to marks.
# Program: Lambda Students Processing

students = [("Amit", 85), ("Priya", 92), ("Rahul", 78), ("Sneha", 88)]

average = lambda marks: sum(m for _, m in marks) / len(marks)
filtered = list(filter(lambda x: x[1] > 75, students))
sorted_students = sorted(students, key=lambda x: x[1])

print("Average:", average(students))
print("Above 75:", filtered)
print("Sorted:", sorted_students)

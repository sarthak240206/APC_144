# Programs on Lambda Function
# Take a list of tuples containing student names and marks, sort the students according to their marks using lambda.
# Program: Lambda Sort Students Marks

students = [("Amit", 85), ("Priya", 92), ("Rahul", 78)]
sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)

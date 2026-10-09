# Create sets representing students enrolled in Python and Java. Find students enrolled in both courses and students enrolled in only one course.
# Program: Enrolled Students

python = {"Amit", "Priya", "Rahul", "Sneha"}
java = {"Priya", "Kiran", "Rahul", "Vijay"}
print("Both:", python & java)
print("Only one:", python ^ java)

# Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
# Program: Student Names

students = {"Amit", "Priya", "Rahul", "Sneha", "Kiran"}
name = input("Enter name: ")
print("Exists" if name in students else "Not Exists")

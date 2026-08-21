students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("\nStudent Records:")
for name, marks in students.items():
    print(name, ":", marks)

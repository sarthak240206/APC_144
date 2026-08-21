# Create a dictionary containing student names and marks. Develop a program to:
# Add a student
# Update marks
# Delete a student
# Search for a student
# Display all students
# Find the highest marks
# Calculate the average

students = {}
while True:
    print("1.Add 2.Update 3.Delete 4.Search 5.Display 6.Highest 7.Average 8.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        name = input("Name: ")
        marks = int(input("Marks: "))
        students[name] = marks
    elif ch == 2:
        name = input("Name: ")
        marks = int(input("New marks: "))
        students[name] = marks
    elif ch == 3:
        name = input("Name: ")
        if name in students:
            del students[name]
    elif ch == 4:
        name = input("Name: ")
        print("Found" if name in students else "Not Found")
    elif ch == 5:
        for k, v in students.items():
            print(k, v)
    elif ch == 6:
        if students:
            print(max(students, key=students.get), max(students.values()))
    elif ch == 7:
        if students:
            print(sum(students.values()) / len(students))
    elif ch == 8:
        break

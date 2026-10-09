name = input("Enter Name: ")
roll_no = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

with open("student.txt", "a") as file:
    file.write(f"\nName: {name}\n")
    file.write(f"Roll Number: {roll_no}\n")
    file.write(f"Branch: {branch}\n")
    file.write(f"Semester: {semester}\n")

print("Student information appended successfully.")

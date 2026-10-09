name = input("Enter Name: ")
roll_no = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

with open("student.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Roll Number: {roll_no}\n")
    file.write(f"Branch: {branch}\n")
    file.write(f"Semester: {semester}\n")

print("Student details written successfully.")

employees = {
    101: "Sarthak",
    102: "Prassana",
    103: "Vyanktesh",
    104: "Balaji"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee ID exists.")
    print("Employee Name:", employees[emp_id])
else:
    print("Employee ID does not exist.")

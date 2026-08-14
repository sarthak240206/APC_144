employees = (
    (101, "sarthak", 45000),
    (102, "Manjunath", 52000),
    (103, "Balaji", 48000),
    (104, "Vaishnavi", 55000)
)

print("Employee Information:")
for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()
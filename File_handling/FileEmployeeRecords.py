def save_employees(filename):
    data = [
        "101,John,IT,65000\n",
        "102,Alice,HR,55000\n",
        "103,Bob,Finance,72000\n",
        "104,Emma,IT,80000\n"
    ]
    with open(filename, "w") as f:
        f.writelines(data)

def display_all(filename):
    print("All Employees:")
    with open(filename, "r") as f:
        for line in f:
            emp_id, name, dept, sal = line.strip().split(",")
            print(f"ID: {emp_id}, Name: {name}, Dept: {dept}, Salary: {sal}")

def highest_paid(filename):
    highest = None
    with open(filename, "r") as f:
        for line in f:
            emp_id, name, dept, sal = line.strip().split(",")
            sal = float(sal)
            if highest is None or sal > highest[3]:
                highest = (emp_id, name, dept, sal)
    if highest:
        print(f"\nHighest-Paid: {highest[1]} (Salary: {highest[3]})")

def average_salary(filename):
    total = 0
    count = 0
    with open(filename, "r") as f:
        for line in f:
            sal = float(line.strip().split(",")[3])
            total += sal
            count += 1
    if count > 0:
        print(f"Average Salary: {total / count:.2f}")

def earning_above(filename, threshold):
    print(f"\nEmployees earning above {threshold}:")
    with open(filename, "r") as f:
        for line in f:
            emp_id, name, dept, sal = line.strip().split(",")
            if float(sal) > threshold:
                print(f"Name: {name}, Salary: {sal}")

file_name = "employees.txt"
save_employees(file_name)
display_all(file_name)
highest_paid(file_name)
average_salary(file_name)
earning_above(file_name, 60000)

# Programs on Lambda Function
# Take employee records containing name and salary, sort them according to salary using lambda.
# Program: Lambda Sort Employees

employees = [("Amit", 60000), ("Priya", 55000), ("Rahul", 75000)]
sorted_emp = sorted(employees, key=lambda x: x[1])

print(sorted_emp)

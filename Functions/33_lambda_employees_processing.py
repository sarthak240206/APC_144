# Programs on Lambda Function
# Take employee records containing name, department, and salary, use filter(), map(), and sorted() with lambda functions to:
# Find employees earning more than 50000. Increase salaries by 10%. Sort employees according to salary.
# Program: Lambda Employees Processing

employees = [("Amit", "CSE", 60000), ("Priya", "IT", 55000), ("Rahul", "ECE", 48000)]

high_earners = list(filter(lambda x: x[2] > 50000, employees))
increased = list(map(lambda x: (x[0], x[1], x[2] * 1.10), employees))
sorted_emp = sorted(employees, key=lambda x: x[2])

print("High earners:", high_earners)
print("Increased salaries:", increased)
print("Sorted:", sorted_emp)

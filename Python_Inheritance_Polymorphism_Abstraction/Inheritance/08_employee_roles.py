class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def salary(self):
        return self.basic_salary


class Manager(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.40


class Developer(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.25


class Tester(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.15


employees = [
    Manager(1, "Amit", 50000),
    Developer(2, "Priya", 45000),
    Tester(3, "Rahul", 40000)
]

for employee in employees:
    print(employee.__class__.__name__, employee.name, "Salary: Rs.", employee.salary())

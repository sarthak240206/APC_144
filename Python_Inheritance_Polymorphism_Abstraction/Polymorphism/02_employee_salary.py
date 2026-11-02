class Employee:
    def calculate_salary(self):
        raise NotImplementedError


class Manager(Employee):
    def __init__(self, basic):
        self.basic = basic

    def calculate_salary(self):
        return self.basic + self.basic * 0.40


class Developer(Employee):
    def __init__(self, basic):
        self.basic = basic

    def calculate_salary(self):
        return self.basic + self.basic * 0.25


class Tester(Employee):
    def __init__(self, basic):
        self.basic = basic

    def calculate_salary(self):
        return self.basic + self.basic * 0.15


for employee in [Manager(50000), Developer(45000), Tester(40000)]:
    print(employee.__class__.__name__, "Salary: Rs.", employee.calculate_salary())

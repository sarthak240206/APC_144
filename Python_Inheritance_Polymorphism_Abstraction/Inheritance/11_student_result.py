class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 3

    def grade(self):
        p = self.percentage()
        if p >= 90:
            return "A+"
        if p >= 80:
            return "A"
        if p >= 70:
            return "B"
        if p >= 60:
            return "C"
        if p >= 40:
            return "D"
        return "Fail"

    def display(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Total:", self.total(), "/ 300")
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())


Result(1, "Amit", "CSE", [85, 90, 78]).display()

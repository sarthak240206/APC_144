class StudentResult:
    def __init__(self, name, marks):
        if len(marks) != 5:
            raise ValueError("Exactly five subject marks are required.")
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 500 * 100

    def grade(self):
        percentage = self.percentage()
        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 40:
            return "D"
        return "F"

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total(), "/ 500")
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

    def __del__(self):
        print("Result object destroyed.")


student = StudentResult("Neha", [85, 90, 78, 92, 88])
student.display()

class Student:
    def __init__(self, roll_no, name, marks, total_marks=500):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.total_marks = total_marks

    def percentage(self):
        return (self.marks / self.total_marks) * 100

    def display(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.percentage(), "%")
        print()


students = [
    Student(1, "Asha", 430),
    Student(2, "Rahul", 390),
    Student(3, "Neha", 465)
]

for student in students:
    student.display()

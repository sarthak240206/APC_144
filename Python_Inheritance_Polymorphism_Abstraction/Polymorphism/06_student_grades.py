class Student:
    def calculate_grade(self, marks):
        return "Grade not defined"


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        p = sum(marks) / len(marks)
        return "A" if p >= 80 else "B" if p >= 60 else "C" if p >= 40 else "Fail"


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        p = sum(marks) / len(marks)
        return "Distinction" if p >= 75 else "Pass" if p >= 50 else "Fail"


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        p = sum(marks) / len(marks)
        return "Excellent" if p >= 85 else "Good" if p >= 65 else "Needs Improvement"


students = [EngineeringStudent(), MedicalStudent(), ManagementStudent()]
marks = [82, 76, 91]
for student in students:
    print(student.__class__.__name__, "Grade:", student.calculate_grade(marks))

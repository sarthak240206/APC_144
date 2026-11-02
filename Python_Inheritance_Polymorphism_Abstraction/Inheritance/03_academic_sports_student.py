class Academic:
    def __init__(self, marks):
        self.marks = marks

    def academic_percentage(self):
        return sum(self.marks) / len(self.marks)


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, name, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)
        self.name = name

    def overall_performance(self):
        return (self.academic_percentage() + self.sports_points) / 2

    def display(self):
        print("Name:", self.name)
        print("Academic Percentage:", self.academic_percentage())
        print("Sports Points:", self.sports_points)
        print("Overall Performance:", self.overall_performance())


student = Student("Amit", [80, 85, 90], 88)
student.display()

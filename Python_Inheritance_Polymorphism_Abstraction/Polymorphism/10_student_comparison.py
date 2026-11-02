class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    def __gt__(self, other):
        return self.total_marks > other.total_marks

    def __lt__(self, other):
        return self.total_marks < other.total_marks


s1 = Student("Amit", 420)
s2 = Student("Priya", 450)
print(s1.name, ">", s2.name, ":", s1 > s2)
print(s1.name, "<", s2.name, ":", s1 < s2)

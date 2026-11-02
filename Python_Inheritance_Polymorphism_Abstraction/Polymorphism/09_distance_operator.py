class Distance:
    def __init__(self, feet, inches):
        total_inches = feet * 12 + inches
        self.feet = total_inches // 12
        self.inches = total_inches % 12

    def __add__(self, other):
        total_inches = self.feet * 12 + self.inches + other.feet * 12 + other.inches
        return Distance(0, total_inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 10)
d2 = Distance(3, 8)
result = d1 + d2
result.display()

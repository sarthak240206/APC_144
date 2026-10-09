# Write a program using separate functions to process student records containing name, roll number, and marks in five subjects.
# Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.
# Program: Student Records

def calculate_total_marks(marks):
    return sum(marks)

def calculate_percentage(total):
    return total / 5

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 60:
        return 'C'
    return 'D'

students = [
    ("Amit", 101, [85, 90, 78, 92, 88]),
    ("Priya", 102, [92, 95, 88, 90, 85]),
    ("Rahul", 103, [70, 75, 68, 72, 80])
]

results = []
for name, roll, marks in students:
    total = calculate_total_marks(marks)
    percentage = calculate_percentage(total)
    grade = calculate_grade(percentage)
    results.append((name, roll, total, percentage, grade))

avg_percentage = sum(r[3] for r in results) / len(results)
highest = max(results, key=lambda x: x[3])
lowest = min(results, key=lambda x: x[3])

for r in results:
    print(f"{r[0]} ({r[1]}): Total={r[2]}, Percentage={r[3]:.2f}, Grade={r[4]}")
print(f"Class Average: {avg_percentage:.2f}")
print(f"Highest: {highest[0]} ({highest[3]:.2f}%)")
print(f"Lowest: {lowest[0]} ({lowest[3]:.2f}%)")

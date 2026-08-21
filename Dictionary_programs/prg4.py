marks = {
    "Sarthak": 75,
    "Prassana": 82,
    "Vyanktesh": 90,
    "Balaji": 88
}

student_name = "Amit"
marks[student_name] = 95

print("Updated marks:")
for name, mark in marks.items():
    print(name, ":", mark)

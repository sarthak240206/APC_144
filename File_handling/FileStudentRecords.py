with open("students_marks.txt", "w") as f:
    f.write("RollNo,Name,Marks\n")
    f.write("101,Amit,85\n")
    f.write("102,Priya,92\n")
    f.write("103,Rahul,78\n")

records = []
with open("students_marks.txt", "r") as f:
    header = f.readline()
    for line in f:
        line = line.strip()
        if line:
            roll, name, marks = line.split(",")
            records.append((roll, name, float(marks)))

print("All Records:")
for r in records:
    print(f"Roll: {r[0]}, Name: {r[1]}, Marks: {r[2]}")

highest = max(records, key=lambda x: x[2])
print("\nHighest Marks:", highest[1], "with", highest[2])

avg_marks = sum(r[2] for r in records) / len(records)
print("Average Marks:", avg_marks)

print("\nStudents scoring more than 80:")
for r in records:
    if r[2] > 80:
        print(f"{r[1]} ({r[2]})")

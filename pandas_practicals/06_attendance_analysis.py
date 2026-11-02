import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Asha", "Rahul", "Neha", "Amit", "Priya"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "CSE"],
    "Total_Classes": [100, 90, 100, 80, 95],
    "Classes_Attended": [90, 60, 72, 70, 80]
}

df = pd.DataFrame(data)
df["Attendance_Percentage"] = df["Classes_Attended"] / df["Total_Classes"] * 100
print(df)
print("\\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])

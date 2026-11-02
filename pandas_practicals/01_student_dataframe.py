import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Asha", "Rahul", "Neha", "Amit", "Priya"],
    "Python": [85, 72, 90, 65, 78],
    "DBMS": [80, 75, 88, 70, 82],
    "Mathematics": [78, 80, 92, 68, 85]
}

df = pd.DataFrame(data)
df["Total"] = df[["Python", "DBMS", "Mathematics"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Mathematics"]].mean(axis=1)

print(df)
print("\\nStudents with average above 75:")
print(df[df["Average"] > 75])

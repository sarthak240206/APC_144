import pandas as pd

data = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Name": ["Anil", "Meera", "Rohan", "Kavita", "Sameer"],
    "Department": ["CSE", "HR", "CSE", "Finance", "IT"],
    "Salary": [60000, 48000, 75000, 52000, 45000],
    "Experience": [5, 8, 3, 10, 2]
}

df = pd.DataFrame(data)
print("Employees earning more than ₹50,000:")
print(df[df["Salary"] > 50000])
print("Average salary:", df["Salary"].mean())
print("Highest salary:", df.loc[df["Salary"].idxmax()])
print("Employee with highest experience:", df.loc[df["Experience"].idxmax()])

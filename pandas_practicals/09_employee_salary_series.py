import pandas as pd

salaries = pd.Series({"Anil": 60000, "Meera": 48000, "Rohan": 75000, "Kavita": 52000, "Sameer": 45000})
print("Salaries:\\n", salaries)
print("Highest salary:", salaries.max())
print("Lowest salary:", salaries.min())
print("Average salary:", salaries.mean())
print("Employees earning more than ₹50,000:\\n", salaries[salaries > 50000])

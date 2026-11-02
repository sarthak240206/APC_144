import pandas as pd

attendance = pd.Series({"Asha": 92, "Rahul": 68, "Neha": 96, "Amit": 74, "Priya": 85})
print("Average attendance:", attendance.mean())
print("Attendance below 75%:\\n", attendance[attendance < 75])
print("Attendance above 90%:\\n", attendance[attendance > 90])
print("Highest attendance:", attendance.idxmax(), attendance.max())

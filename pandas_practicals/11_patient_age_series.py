import pandas as pd

ages = pd.Series({"P001": 65, "P002": 45, "P003": 72, "P004": 30, "P005": 61})
print("Average age:", ages.mean())
print("Oldest patient:", ages.idxmax(), "Age:", ages.max())
print("Youngest patient:", ages.idxmin(), "Age:", ages.min())
print("Patients above 60 years:\\n", ages[ages > 60])

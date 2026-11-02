import pandas as pd

df = pd.read_csv("patients.csv")
print("Patients above 60 years:\\n", df[df["Age"] > 60])
print("Average medical expense:", df["Medical_Expense"].mean())
print("Patient with highest medical expense:\\n", df.loc[df["Medical_Expense"].idxmax()])
print("\\nPatient count for each disease:\\n", df["Disease"].value_counts())
print("\\nPatients with medical expense above ₹50,000:\\n", df[df["Medical_Expense"] > 50000])

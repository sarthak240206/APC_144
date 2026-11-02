import pandas as pd

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Name": ["Ramesh", "Sita", "Mohan", "Geeta", "Arun"],
    "Age": [65, 45, 72, 30, 61],
    "Disease": ["Diabetes", "Asthma", "Heart Disease", "Flu", "Diabetes"],
    "Medical_Charges": [60000, 12000, 85000, 5000, 52000]
}

df = pd.DataFrame(data)
print("Patients above 60:")
print(df[df["Age"] > 60])
print("Average medical charge:", df["Medical_Charges"].mean())
print("Maximum medical charge:", df["Medical_Charges"].max())
print("Patients with charges above ₹50,000:")
print(df[df["Medical_Charges"] > 50000])

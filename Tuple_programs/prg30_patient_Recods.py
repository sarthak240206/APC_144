

patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Priya", 32, "B+"),
    (103, "Amit", 45, "O+"),
    (104, "Sneha", 28, "A+"),
    (105, "Rohan", 50, "O-")
)


print("ALL PATIENT RECORDS")
print("-" * 40)

for patient in patients:
    print("Patient ID:", patient[0])
    print("Name:", patient[1])
    print("Age:", patient[2])
    print("Blood Group:", patient[3])
    print()

search_id = int(input("Enter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == search_id:
        print("\nPatient Found:")
        print("Patient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True
        break

if not found:
    print("Patient not found.")

print("\nTotal number of patients:", len(patients))


blood_group = input("\nEnter blood group to search: ").upper()

print("\nPatients with blood group", blood_group, ":")
found = False

for patient in patients:
    if patient[3] == blood_group:
        print(
            "ID:", patient[0],
            "| Name:", patient[1],
            "| Age:", patient[2],
            "| Blood Group:", patient[3]
        )
        found = True

if not found:
    print("No patients found with this blood group.")
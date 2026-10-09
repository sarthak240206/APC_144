# Create two sets of students present in morning and afternoon sessions. Find students present in both, only morning, only afternoon, and at least one session.
# Program: Students Sessions

morning = {"Amit", "Priya", "Rahul"}
afternoon = {"Priya", "Sneha", "Kiran"}
print("Both:", morning & afternoon)
print("Only morning:", morning - afternoon)
print("Only afternoon:", afternoon - morning)
print("At least one:", morning | afternoon)

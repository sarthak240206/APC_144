

salary = {
    "sarthak": 60000,
    "om": 55000,
    "ram": 28000,
    "Sneha": 75000
}
print("Highest:", max(salary, key=salary.get), max(salary.values()))
print("Lowest:", min(salary, key=salary.get), min(salary.values()))
print("Average:", sum(salary.values()) / len(salary))
above = [k for k, v in salary.items() if v > 50000]
print("Above 50000:", above)

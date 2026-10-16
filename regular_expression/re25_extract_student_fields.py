import re

text = input("Enter details (example: Name: Rahul, Roll: 101, Marks: 85): ")
pattern = r"Name:\\s*([A-Za-z]+),\\s*Roll:\\s*(\\d+),\\s*Marks:\\s*(\\d+)"

matches = re.findall(pattern, text)
if matches:
    for name, roll, marks in matches:
        print("Name:", name)
        print("Roll number:", roll)
        print("Marks:", marks)
else:
    print("No matching student record found.")

import re

number = input("Enter vehicle registration number (example MH12AB1234): ")
pattern = r"[A-Z]{2}\\d{2}[A-Z]{2}\\d{4}"

if re.fullmatch(pattern, number):
    print("Matches the common format")
else:
    print("Does not match the common format")

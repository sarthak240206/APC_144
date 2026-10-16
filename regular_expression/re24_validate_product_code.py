import re

code = input("Enter product code (example ABC-1234-XY): ")
pattern = r"[A-Z]{3}-\\d{4}-[A-Z]{2}"

if re.fullmatch(pattern, code):
    print("Valid product code")
else:
    print("Invalid product code")

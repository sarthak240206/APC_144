import re

email = input("Enter an email address: ")
pattern = r"[\\w.-]+@[\\w.-]+\\.[A-Za-z]{2,}"

if re.fullmatch(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

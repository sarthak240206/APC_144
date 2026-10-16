import re

text = input("Enter a paragraph: ")
print("Dates (DD-MM-YYYY):", re.findall(r"\\b\\d{2}-\\d{2}-\\d{4}\\b", text))

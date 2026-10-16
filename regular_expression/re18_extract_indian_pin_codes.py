import re

text = input("Enter a paragraph: ")
print("Six-digit PIN codes:", re.findall(r"\\b[1-9]\\d{5}\\b", text))

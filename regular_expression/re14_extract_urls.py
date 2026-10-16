import re

text = input("Enter text: ")
print("URLs:", re.findall(r"https?://\\S+", text))

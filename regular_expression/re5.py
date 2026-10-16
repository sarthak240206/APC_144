import re

text = input("Enter text (you can include spaces and tabs): ")
print("Spaces, tabs, and newlines:", re.findall(r"[ \\t\\n]", text))

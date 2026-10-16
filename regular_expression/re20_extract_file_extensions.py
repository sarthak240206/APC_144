import re

text = input("Enter filenames or text containing filenames: ")
print("File extensions:", re.findall(r"\\.([A-Za-z0-9]+)\\b", text))

import re

text = input("Enter a string: ")
print("Updated text:", re.sub(r" +", " ", text))

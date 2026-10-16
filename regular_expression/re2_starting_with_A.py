import re

sentence = input("Enter a sentence: ")
print("Words starting with A/a:", re.findall(r"\\b[Aa]\\w*", sentence))

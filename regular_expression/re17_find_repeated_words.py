import re

sentence = input("Enter a sentence: ")
pattern = r"\\b(\\w+)\\s+\\1\\b"
print("Repeated consecutive words:", re.findall(pattern, sentence, re.IGNORECASE))

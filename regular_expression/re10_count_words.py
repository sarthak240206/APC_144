import re

sentence = input("Enter a sentence: ")
words = re.findall(r"\\b\\w+\\b", sentence)
print("Word count:", len(words))

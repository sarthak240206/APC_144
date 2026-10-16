import re

text = input("Enter a string: ")
vowels = re.findall(r"[aeiouAEIOU]", text)
print("Vowel count:", len(vowels))

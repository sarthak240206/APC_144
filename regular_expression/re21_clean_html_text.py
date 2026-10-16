import re

text = input("Enter text containing HTML tags: ")
text = re.sub(r"<[^>]*>", " ", text)
text = re.sub(r"[^\\w\\s.,!?]", "", text)
text = re.sub(r"\\s+", " ", text).strip()
print("Cleaned text:", text)

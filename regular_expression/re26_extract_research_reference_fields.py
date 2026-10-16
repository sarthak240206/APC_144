import re

text = input("Enter research paper references: ")

doi_pattern = r"\\b10\\.\\d{4,9}/[^\\s]+"
email_pattern = r"[\\w.-]+@[\\w.-]+\\.[A-Za-z]{2,}"
url_pattern = r"https?://\\S+"
year_pattern = r"\\b(?:19|20)\\d{2}\\b"

print("DOI identifiers:", re.findall(doi_pattern, text))
print("Publication years:", re.findall(year_pattern, text))
print("Email addresses:", re.findall(email_pattern, text))
print("URLs:", re.findall(url_pattern, text))

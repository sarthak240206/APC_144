import re

post = input("Enter a social media post: ")
print("Hashtags:", re.findall(r"#[A-Za-z0-9_]+", post))

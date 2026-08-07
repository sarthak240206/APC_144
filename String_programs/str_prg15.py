s = input("Enter a string: ")
duplicates = []
seen = set()

for ch in s:
    if ch in seen and ch not in duplicates:
        duplicates.append(ch)
    else:
        seen.add(ch)

print("Duplicate characters:", " ".join(duplicates))

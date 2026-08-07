s = input("Enter a string: ")
ch = input("Enter character to find: ")
count = 0

for c in s:
    if c == ch:
        count += 1

print("Frequency:", count)

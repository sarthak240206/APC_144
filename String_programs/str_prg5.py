s = input("Enter a string: ")
uppercase = lowercase = 0

for ch in s:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)

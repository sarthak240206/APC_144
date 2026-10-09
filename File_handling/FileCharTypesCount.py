filename = input("Enter file name: ")

alphabets = 0
digits = 0
spaces = 0
special = 0

try:
    with open(filename, "r") as file:
        text = file.read()
        for ch in text:
            if ch.isalpha():
                alphabets += 1
            elif ch.isdigit():
                digits += 1
            elif ch.isspace():
                spaces += 1
            else:
                special += 1
        print("Alphabets:", alphabets)
        print("Digits:", digits)
        print("Spaces:", spaces)
        print("Special characters:", special)
except FileNotFoundError:
    print("File not found.")

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in reversed(lines):
            print(line.rstrip())
except FileNotFoundError:
    print("File not found.")

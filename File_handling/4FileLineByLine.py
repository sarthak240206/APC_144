filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")

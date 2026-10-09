filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        print("Total number of words:", len(words))
except FileNotFoundError:
    print("File not found.")

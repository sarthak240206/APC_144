filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        text = file.read()
        print("Total number of characters (including spaces):", len(text))
except FileNotFoundError:
    print("File not found.")

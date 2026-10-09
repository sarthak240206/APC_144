filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        words = file.read().split()
        if words:
            longest = max(words, key=len)
            print("Longest word:", longest)
            print("Length:", len(longest))
        else:
            print("File is empty.")
except FileNotFoundError:
    print("File not found.")

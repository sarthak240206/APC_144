filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        words = file.read().split()
        frequency = {}
        for word in words:
            word = word.strip(".,!?;:\"'()[]{}").lower()
            if word:
                frequency[word] = frequency.get(word, 0) + 1
        print(frequency)
except FileNotFoundError:
    print("File not found.")

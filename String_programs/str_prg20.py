sentence = input("Enter a sentence: ")
word = input("Enter word to count: ")

words = sentence.split()
count = 0

for w in words:
    if w.lower() == word.lower():
        count += 1

print("Occurrences:", count)

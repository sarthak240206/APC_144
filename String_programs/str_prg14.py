sentence = input("Enter a sentence: ")
words = sentence.split()
result = []

for word in words:
    if word:
        result.append(word[0].upper() + word[1:])

print("Title case:", " ".join(result))

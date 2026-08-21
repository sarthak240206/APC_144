paragraph = input("Enter a paragraph: ")

words = paragraph.split()
word_length = {}

for word in words:
    length = len(word)

    if length in word_length:
        word_length[length] += 1
    else:
        word_length[length] = 1

print("Word length dictionary:")

for length, count in word_length.items():
    print(length, ":", count)

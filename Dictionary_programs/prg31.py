words = ["cat", "dog", "apple", "bat", "banana", "car"]

word_dict = {}

for word in words:
    length = len(word)

    if length not in word_dict:
        word_dict[length] = []

    word_dict[length].append(word)

print("Dictionary:", word_dict)

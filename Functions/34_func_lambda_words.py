# functions, map(), filter(), and lambda expressions to process a list of words and:
# Find the length of every word. Extract words having more than five characters. Sort words according to their length.
# Program: Lambda Words Processing

words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

lengths = list(map(lambda w: len(w), words))
long_words = list(filter(lambda w: len(w) > 5, words))
sorted_words = sorted(words, key=lambda w: len(w))

print("Lengths:", lengths)
print("Long words:", long_words)
print("Sorted:", sorted_words)

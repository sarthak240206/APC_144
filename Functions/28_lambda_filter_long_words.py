# Programs on Lambda Function
# Take a list of words, use filter() and lambda to find words having more than five characters.
# Program: Lambda Filter Long Words

words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda w: len(w) > 5, words))

print(long_words)

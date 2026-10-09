# Programs on Lambda Function
# Take a list of words; sort them according to their length using lambda.
# Program: Lambda Sort Words Length

words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda w: len(w))

print(sorted_words)

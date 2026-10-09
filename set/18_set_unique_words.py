# Accept a sentence from the user and use a set to display all unique words.
# Program: Unique Words

sentence = input("Enter sentence: ")
words = sentence.split()
print(set(words))

# Accept a sentence and create a dictionary containing each word and the number of times it occurs.

s = input("Enter a sentence: ")
words = s.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

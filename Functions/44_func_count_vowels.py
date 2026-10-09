# Define a function that accepts a string and returns the number of vowels present in it.
# Program: Count Vowels

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

print(count_vowels("Hello World"))

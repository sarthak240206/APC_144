import string_utils

text = input("Enter a string: ")

print("Vowel Count:", string_utils.count_vowels(text))
print("Reversed String:", string_utils.reverse_string(text))
print("Is Palindrome:", string_utils.is_palindrome(text))
print("Word Count:", string_utils.count_words(text))
print("Without Spaces:", string_utils.remove_spaces(text))

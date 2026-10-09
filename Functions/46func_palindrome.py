# Create a function that checks whether a given string or number is a palindrome.
# Program: Palindrome

def is_palindrome(val):
    s = str(val)
    return s == s[::-1]

print(is_palindrome("madam"))
print(is_palindrome(121))

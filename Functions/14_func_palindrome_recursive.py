# Check whether a string is a palindrome using recursion.
# Program: Palindrome Recursive

def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

print(is_palindrome_recursive("madam"))

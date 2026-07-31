n = int(input("Enter num to check sum of digits"))
s = n
rev = 0
while(n>0):
    rem = n%10
    rev = rev*10+rem
    n = n//10
if s == rev:
    print("Entered number is palindrome")
else:
    print("Entered number is not palindrome")

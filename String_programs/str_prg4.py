s = input("Enter String")
rev=" "
for i in s:
    rev = i+rev

if s == rev:
    print("Entered String",s,"is palindrome")

s = input("Enter String")
s.lower()
x = "aeiou"
vcount=0
concount=0
numcount=0
spaces=0
spchar=0
for i in s:
    if i.isalpha():
        if i in x:
            vcount=vcount+1
        else:
            concount+=1
    if i.isnumeric():
        numcount+=1

    if i == " ":
        spaces+=1

    else:
        spchar+=1

print("Vowels",vcount)
print("Consonant",concount)
print("Number count",numcount)
print("space count",spaces)
print("special characters",spchar)

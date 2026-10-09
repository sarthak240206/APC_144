f = open("sample.txt","r")
text = f.read()
print(text)
vcount = 0 
ccount = 0 
dcount = 0 
scount = 0 
for i in text:
    if i.isalpha():
        if i.lower() in "aeiou":
            vcount+=1
        else:
            ccount+=1
    elif i.isdigit():
        dcount+=1
    else:
        scount+=1

print(text)
print(vcount)
print(ccount)
print(dcount)
print(scount)
f.close()
li = [1,5,2,1,5,6,7,46,85,58,5,3,7,8]
unique=[]
for i in li:
    if i not in unique:
        unique.append(i)

print("Original list",li)
print("List containing only unique elements",unique)

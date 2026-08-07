li = [15,78,4,6,100,10000,5,3]
great = li[0]
slargest = -1
for i in li:
    if i > great:
        great = i

for j in li:
    if j>slargest and j<great:
        slargest = j
print(li)
print("Second largest element of list",slargest)

li = [10,56,82,34,60,20,5,54,64,621,100,1,6]
small = li[0]
great = li[0]

for i in li:
    if i > great:
        great = i

    if i<small:
        small = i

print(li)
print("Greatest element from list")
print(great)
print("Smallest element from list")
print(small)

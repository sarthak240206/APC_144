tup =78,56,34,12,34,90,115,73,38,11,300.98,10000,45


print("The tuple is:", tup)
even = 0
odd = 0
for i in range(len(tup)):
    if tup[i] % 2 == 0:
        even += 1
    else:
        odd += 1
print("The number of even elements in the tuple is:", even)
print("The number of odd elements in the tuple is:", odd)
numbers=list(map(int,input("List elements: ").split()))
result=[]
for x in numbers:
    if x not in result:
        result.append(x)
print("After removing duplicates:",result)

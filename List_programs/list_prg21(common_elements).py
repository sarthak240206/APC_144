list1=list(map(int,input("First list: ").split()))
list2=list(map(int,input("Second list: ").split()))
common=[]
for x in list1:
    if x in list2 and x not in common:
        common.append(x)
print("Common elements:",common)

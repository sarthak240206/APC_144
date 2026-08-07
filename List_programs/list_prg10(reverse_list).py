li = ['A','B','C','D','E','F','G','H','I']
print(li)
size = len(li)-1
i = 0
while(i<size):
    li[i]=li[size]
    li[size]=li[i]
    i=i+1;
    size=size-1;
print("List after reverse")
print(li)

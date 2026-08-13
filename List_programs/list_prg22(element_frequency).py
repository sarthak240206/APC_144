numbers=list(map(int,input("List elements: ").split()))
freq={}
for x in numbers:
    freq[x]=freq.get(x,0)+1
for x,count in freq.items():
    print(x,":",count)

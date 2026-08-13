items=[]
n=int(input("Enter number of items: "))
for i in range(n):
    items.append(input(f"Enter item {i+1}: "))
print("Stored items:",items)
print("Total items:",len(items))

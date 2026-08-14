list1 = []
for i in range(1,6):
    ele = int(input("Enter an element to add to the list: "))
    list1.append(ele)

tup = tuple(list1)
print("The list is:", list1)
print("The tuple is:", tup)
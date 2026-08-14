tup = 10,20,30,40,50
print("The tuple is:", tup)
list1 = list(tup)
print("The list is:", list1)
list1.append(60)
list1.append(70)
print("The list after adding new elements to it is:", list1)
tup = tuple(list1)
print("The tuple after adding new elements to it is:", tup)
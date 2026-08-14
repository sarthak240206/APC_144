tup =78,56,34,12,34,90,115,73,38,11,300.98,10000,45
print("The tuple is:", tup)
target = int(input("Enter an element to check if it is present in the tuple or not: "))
if target in tup:
    print("The element is present in the tuple.")
else:
    print("The element is not present in the tuple.")
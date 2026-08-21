set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1)
print(set2)
if set1.isdisjoint(set2):
    print("The sets have no elements in common")
else:
    print("The sets have elements in common")
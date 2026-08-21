set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print(set1)
print(set2)
if set1.issuperset(set2):
    print("First set is a superset of the second set")
else:
    print("First set is not a superset of the second set")
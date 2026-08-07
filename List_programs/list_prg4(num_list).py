num_list = [150,236,56,93,8,72]
print("List before update")
for i in num_list:
    print(i)

print("Insertion at begining")
num_list.insert(0,1000)
print(num_list)
print("Insertion at end")
num_list.append(5000)
print(num_list)
print("Insertion at Specified position")
num_list.insert(4,8888)
print("List after update")
for i in num_list:
    print(i)

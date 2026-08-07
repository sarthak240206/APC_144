num = []
for i in range(11):
    s = int(input("Enter Element"))
    num.append(s)
print("List before sorting")
print(num)
num.sort()
print("List sorted in ascending order",num)
num.sort(reverse = True)
print("List sorted in Descending order",num)

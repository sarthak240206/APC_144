num = []
for i in range(16):
    s = int(input("Enter Element"))
    num.append(s)

even_count = 0
odd_count = 0
for i in num:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(num)
print("count of even numbers from list is",even_count)
print("count of odd numbers from list is",odd_count)

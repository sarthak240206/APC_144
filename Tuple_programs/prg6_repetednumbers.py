num = (1,2,3,4,1,9,2,1,4,5,3,1,2,4)
target = int(input("Enter a number to check how many times it is repeated in the tuple: "))
count = 0
for i in num:
    if i == target:
        count+=1
print(count)
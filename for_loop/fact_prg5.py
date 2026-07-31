n = int(input("Enter number"))
fact = 1
sum = 1
for i in range(1,n+1):
    fact = i*fact
    sum = sum+(1//fact)
print(sum)

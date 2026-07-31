n = int(input("Enter num to check sum of digits"))
s = n
sum = 0
while(n>0):
    rem = n%10
    sum = rem+sum
    n = n//10

print("Sum of digits of num",s,"is",sum)

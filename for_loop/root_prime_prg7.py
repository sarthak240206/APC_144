import math
n = int(input("Enter number"))
sqr = int(math.sqrt(n))
cnt = 0
for i in range(1,sqr+1):
    if sqr%i==0:
        cnt=cnt+1

if cnt==2:
    print("Square root of number",n,"is",sqr,"is prime")
else:
    print("Square root of number",n,"is",sqr,"is not prime")

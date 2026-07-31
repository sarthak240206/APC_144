n= int(input("enter a number"))
i=0
fib_no=0
sno=1
print(fib_no)
print(sno)
while(i<=n):
    tno=fib_no+sno
    print(tno)
    i+=1
    fib_no=sno
    sno=tno

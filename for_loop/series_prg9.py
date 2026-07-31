n = int(input("Enter number"))
l = 65
for i in range(1,n+1):
    for j in range(i):
        print(chr(l+j),end=" ")

    print("\n")

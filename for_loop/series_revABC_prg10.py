n = int(input("Enter number"))
l = 65
for i in range(n,0,-1):
    for j in range(i):
        print(chr(l+j),end=" ")

    print("\n")

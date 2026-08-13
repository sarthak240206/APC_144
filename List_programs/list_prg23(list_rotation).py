numbers=list(map(int,input("List elements: ").split()))
if numbers:
    print("Left rotation:",numbers[1:]+numbers[:1])
    print("Right rotation:",numbers[-1:]+numbers[:-1])
else:
    print("List is empty")

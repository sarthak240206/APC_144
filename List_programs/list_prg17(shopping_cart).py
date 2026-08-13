cart=[]
while True:
    print("\n1.Add 2.Remove 3.Search 4.Display 5.Count 6.Exit")
    c=input("Choice: ")
    if c=="1": cart.append(input("Item: "))
    elif c=="2":
        x=input("Item: ")
        if x in cart: cart.remove(x)
        else: print("Item not found")
    elif c=="3":
        x=input("Item: ")
        print("Item found" if x in cart else "Item not found")
    elif c=="4": print(cart)
    elif c=="5": print("Total items:",len(cart))
    elif c=="6": break

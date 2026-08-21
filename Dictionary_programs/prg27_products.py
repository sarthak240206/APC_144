products = {}
while True:
    print("1.Add 2.Update 3.Delete 4.Search 5.Display 6.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        name = input("Product: ")
        qty = int(input("Quantity: "))
        products[name] = qty
    elif ch == 2:
        name = input("Product: ")
        qty = int(input("New qty: "))
        products[name] = qty
    elif ch == 3:
        name = input("Product: ")
        if name in products:
            del products[name]
    elif ch == 4:
        name = input("Product: ")
        print("Found" if name in products else "Not Found")
    elif ch == 5:
        for k, v in products.items():
            if v < 10:
                print(k, v)
    elif ch == 6:
        break

books=[]
while True:
    print("\n1.Add 2.Search 3.Remove 4.Display 5.Count 6.Exit")
    c=input("Choice: ")
    if c=="1": books.append(input("Book name: "))
    elif c=="2":
        x=input("Book name: ")
        print("Book found" if x in books else "Book not found")
    elif c=="3":
        x=input("Book name: ")
        if x in books: books.remove(x)
        else: print("Book not found")
    elif c=="4": print(books)
    elif c=="5": print("Total books:",len(books))
    elif c=="6": break

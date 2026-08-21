# Create a dictionary containing book IDs and book names.
# Implement:
# Add a book
# Search a book
# Remove a book
# Display all books
# Count total books

books = {}
while True:
    print("1.Add 2.Search 3.Remove 4.Display 5.Count 6.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        bid = input("ID: ")
        bname = input("Name: ")
        books[bid] = bname
    elif ch == 2:
        bid = input("ID: ")
        print(books.get(bid, "Not Found"))
    elif ch == 3:
        bid = input("ID: ")
        if bid in books:
            del books[bid]
    elif ch == 4:
        for k, v in books.items():
            print(k, v)
    elif ch == 5:
        print(len(books))
    elif ch == 6:
        break

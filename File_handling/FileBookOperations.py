def add_book(book_id, title, author, status="Available"):
    with open("books.txt", "a") as f:
        f.write(f"{book_id},{title},{author},{status}\n")

def search_book(title):
    found = False
    with open("books.txt", "r") as f:
        for line in f:
            b_id, b_title, author, status = line.strip().split(",")
            if b_title.lower() == title.lower():
                print(f"Found: ID={b_id}, Title={b_title}, Author={author}, Status={status}")
                found = True
    if not found:
        print("Book not found.")

def update_status(book_id, new_status):
    lines = []
    updated = False
    with open("books.txt", "r") as f:
        for line in f:
            b_id, title, author, status = line.strip().split(",")
            if b_id == book_id:
                lines.append(f"{b_id},{title},{author},{new_status}\n")
                updated = True
            else:
                lines.append(line)
    with open("books.txt", "w") as f:
        f.writelines(lines)
    return updated

def issue_book(book_id):
    if update_status(book_id, "Issued"):
        print(f"Book {book_id} issued successfully.")
    else:
        print(f"Book {book_id} not found.")

def return_book(book_id):
    if update_status(book_id, "Available"):
        print(f"Book {book_id} returned successfully.")
    else:
        print(f"Book {book_id} not found.")

def display_available():
    print("Available Books:")
    with open("books.txt", "r") as f:
        for line in f:
            b_id, title, author, status = line.strip().split(",")
            if status == "Available":
                print(f"ID: {b_id}, Title: {title}, Author: {author}")

with open("books.txt", "w") as f:
    pass

add_book("B101", "Python Basics", "Guido", "Available")
add_book("B102", "Data Structures", "Mark", "Available")
add_book("B103", "Algorithms", "CLRS", "Available")

search_book("Python Basics")
issue_book("B101")
display_available()
return_book("B101")
display_available()

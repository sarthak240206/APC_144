# Create functions to add books, issue books, return books, search books, and display available books.
# Maintain book availability using dictionaries.
# Program: Library

books = {}

def add_book(book_id, book_name):
    books[book_id] = book_name

def issue_book(book_id):
    if book_id in books:
        print(f"Issued: {books[book_id]}")
        del books[book_id]
    else:
        print("Not available")

def return_book(book_id, book_name):
    books[book_id] = book_name

def search_book(book_id):
    print(books.get(book_id, "Not Found"))

def display_books():
    for k, v in books.items():
        print(k, v)

add_book(1, "Python 101")
add_book(2, "Data Science")
display_books()

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price: ₹", self.price)
        print()


books = [
    Book(1, "Wings of Fire", "A. P. J. Abdul Kalam", 250),
    Book(2, "The Alchemist", "Paulo Coelho", 300),
    Book(3, "Atomic Habits", "James Clear", 450)
]

for book in books:
    book.display()

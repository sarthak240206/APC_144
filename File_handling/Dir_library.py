import os
import sys

sys.path.insert(0, os.path.abspath("library_app"))

from books.catalog import get_book_info
from members.member_ops import get_member_info
from transactions.borrow import borrow_book

book = get_book_info("B001", "Introduction to Algorithms", "Thomas Cormen")
member = get_member_info("M501", "Aditya Roy")
record = borrow_book(member["name"], book["title"])

print("Book:", book)
print("Member:", member)
print("Transaction:", record)

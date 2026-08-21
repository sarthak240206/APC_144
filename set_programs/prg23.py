available_books = {"Python Basics", "Java Programming", "Data Science", "Web Development"}
requested_books = {"Python Basics", "Data Science", "Machine Learning"}

available_requested = available_books & requested_books

print("Requested books that are available:", available_requested)
# Create a set containing available books and another set containing requested books. Determine which requested books are available.
# Program: Books Available

available = {"Python 101", "Data Science", "AI Basics", "Web Dev"}
requested = {"AI Basics", "Cyber Security", "Python 101"}
print("Available requested:", available & requested)

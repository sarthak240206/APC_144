students = {"sarthak","prassana","vaishnavi","varad"}
name = input("Enter your name: ").lower()
if name in students:
    print("Your name is present in the set")
else:
    print("Your name is not present in the set")
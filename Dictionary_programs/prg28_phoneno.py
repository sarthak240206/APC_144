# Create a dictionary containing names and phone numbers.
# Implement:
# Add contact
# Search contact
# Update contact
# Delete contact
# Display all contacts

contacts = {}
while True:
    print("1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
    elif ch == 2:
        name = input("Name: ")
        print(contacts.get(name, "Not Found"))
    elif ch == 3:
        name = input("Name: ")
        phone = input("New phone: ")
        contacts[name] = phone
    elif ch == 4:
        name = input("Name: ")
        if name in contacts:
            del contacts[name]
    elif ch == 5:
        for k, v in contacts.items():
            print(k, v)
    elif ch == 6:
        break

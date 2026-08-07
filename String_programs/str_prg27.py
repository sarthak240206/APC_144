email = input("Enter email address: ")

if email.count("@") == 1:
    username, domain = email.split("@")

    if (username and domain and
        "." in domain and
        not domain.startswith(".") and
        not domain.endswith(".") and
        " " not in email):
        print("Valid email")
    else:
        print("Invalid email")
else:
    print("Invalid email")

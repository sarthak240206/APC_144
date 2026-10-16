class ATM:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        print("Current balance: ₹", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Enter a positive amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a positive amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def display_details(self):
        print("Account holder:", self.account_holder)
        print("Account number:", self.account_number)
        print("Balance: ₹", self.balance)


atm = ATM("Pradnya", "1234567890", 5000)

while True:
    print("\\n1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display account details")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        try:
            atm.deposit(float(input("Enter amount to deposit: ₹")))
        except ValueError:
            print("Enter a valid number.")
    elif choice == "3":
        try:
            atm.withdraw(float(input("Enter amount to withdraw: ₹")))
        except ValueError:
            print("Enter a valid number.")
    elif choice == "4":
        atm.display_details()
    elif choice == "5":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice.")

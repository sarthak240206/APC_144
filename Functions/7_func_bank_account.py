# Create functions for deposit, withdrawal, balance enquiry, and transaction history.
# Prevent withdrawal when the balance is insufficient and maintain a transaction record.
# Program: Bank Account

balance = 1000
history = []

def deposit(amount):
    global balance
    balance += amount
    history.append(f"Deposited: {amount}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        history.append(f"Withdrawn: {amount}")

def balance_enquiry():
    print(f"Balance: {balance}")

def transaction_history():
    for h in history:
        print(h)

deposit(500)
withdraw(300)
balance_enquiry()
transaction_history()

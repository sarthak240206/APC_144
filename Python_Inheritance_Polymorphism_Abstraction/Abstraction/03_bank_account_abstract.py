from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance + 1000:
            self.balance -= amount


for account in [SavingsAccount(5000), CurrentAccount(5000)]:
    account.deposit(1000)
    account.withdraw(2000)
    print(account.__class__.__name__, "Balance: Rs.", account.balance)

class BankAccount:
    def __init__(self, balance, rate):
        self.balance = balance
        self.rate = rate

    def calculate_interest(self):
        return self.balance * self.rate / 100


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.04


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return 0


class FixedDepositAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.07


for account in [SavingsAccount(50000, 4), CurrentAccount(50000, 0), FixedDepositAccount(50000, 7)]:
    print(account.__class__.__name__, "Interest: Rs.", account.calculate_interest())

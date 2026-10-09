from banking.account import create_account, get_balance
from banking.transaction import deposit, withdraw
from banking.loan import calculate_emi

acc = create_account(101, "Alice", 10000)
print("Account created:", acc)

acc = deposit(acc, 5000)
print("After deposit:", get_balance(acc))

acc = withdraw(acc, 3000)
print("After withdrawal:", get_balance(acc))

emi = calculate_emi(principal=500000, rate=8.5, tenure_years=5)
print("Monthly Loan EMI:", round(emi, 2))

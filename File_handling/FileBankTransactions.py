transactions = [
    "deposit,5000\n",
    "withdraw,1500\n",
    "deposit,2000\n",
    "withdraw,3000\n",
    "deposit,7000\n"
]

with open("transactions.txt", "w") as f:
    f.writelines(transactions)

total_deposits = 0
total_withdrawals = 0
largest_tx_type = ""
largest_tx_amount = 0

with open("transactions.txt", "r") as f:
    for line in f:
        tx_type, amount = line.strip().split(",")
        amount = float(amount)
        if tx_type == "deposit":
            total_deposits += amount
        elif tx_type == "withdraw":
            total_withdrawals += amount
        if amount > largest_tx_amount:
            largest_tx_amount = amount
            largest_tx_type = tx_type

final_balance = total_deposits - total_withdrawals

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", final_balance)
print(f"Largest Transaction: {largest_tx_type} of {largest_tx_amount}")

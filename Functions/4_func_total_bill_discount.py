# Create a function that accepts item prices and quantities and returns the total bill after applying a discount.
# Program: Total Bill Discount

def total_bill(prices, quantities):
    subtotal = sum(p * q for p, q in zip(prices, quantities))
    if subtotal > 10000:
        discount = subtotal * 0.10
    else:
        discount = 0
    return subtotal - discount

print(total_bill([100, 200, 300], [2, 1, 3]))

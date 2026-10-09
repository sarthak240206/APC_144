# Develop a modular program using functions to calculate electricity bills using different consumption slabs.
# Include fixed charges, taxes, and discounts.
# Program: Electricity Bill Modular

def calculate_bill(units):
    fixed_charge = 100
    if units <= 100:
        charge = units * 5
    elif units <= 200:
        charge = 100 * 5 + (units - 100) * 7
    else:
        charge = 100 * 5 + 100 * 7 + (units - 200) * 10
    tax = charge * 0.05
    total = charge + fixed_charge + tax
    return total

print(calculate_bill(250))

# Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill.
# Apply discounts based on patient category.
# Program: Hospital Billing

def consultation(charges):
    return charges

def lab_charges(charges):
    return charges

def medicine_charges(charges):
    return charges

def room_charges(days, rate):
    return days * rate

def final_bill(consult, lab, medicine, room, category):
    total = consult + lab + medicine + room
    if category == "senior":
        total *= 0.9
    return total

print(final_bill(500, 1000, 800, 2000, "senior"))

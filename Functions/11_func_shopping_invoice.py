# Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.
# Program: Shopping Invoice

products = []

def add_product(name, price, qty):
    products.append((name, price, qty))

def remove_product(name):
    global products
    products = [p for p in products if p[0] != name]

def subtotal():
    return sum(p[1] * p[2] for p in products)

def apply_discount(total):
    return total * 0.9 if total > 10000 else total

def calculate_gst(total):
    return total * 0.18

def final_invoice():
    sub = subtotal()
    disc = apply_discount(sub)
    gst = calculate_gst(disc)
    print(f"Subtotal: {sub}, Discount: {disc}, GST: {gst}, Total: {disc + gst}")

add_product("Laptop", 50000, 1)
add_product("Mouse", 500, 2)
final_invoice()

products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 9000
}

products["Headphones"] = 2000

print("Updated product dictionary:")
for product, price in products.items():
    print(product, ":", price)

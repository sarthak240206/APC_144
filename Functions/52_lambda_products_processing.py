# Programs on Lambda Function
# Take a list of products with names, prices, and quantities, use functions and lambda expressions to:
# Calculate total value of each product. Filter products costing more than 1000. Sort products according to total value.
# Program: Lambda Products Processing

products = [("Laptop", 50000, 1), ("Mouse", 500, 2), ("Keyboard", 1200, 1)]

total_value = list(map(lambda p: (p[0], p[1] * p[2]), products))
filtered = list(filter(lambda p: p[1] > 1000, total_value))
sorted_products = sorted(total_value, key=lambda x: x[1])

print("Total value:", total_value)
print("Filtered:", filtered)
print("Sorted:", sorted_products)

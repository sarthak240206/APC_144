import pandas as pd

prices = pd.Series({"Laptop": 55000, "Mouse": 700, "Monitor": 12000, "Keyboard": 1500})
print("Original prices:\\n", prices)
updated = prices * 1.10
print("\\nPrices after 10% increase:\\n", updated)
print("Most expensive product:", prices.idxmax(), "at ₹", prices.max())
print("Products costing more than ₹1,000:\\n", prices[prices > 1000])

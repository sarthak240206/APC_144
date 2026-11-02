import pandas as pd

data = {
    "Order_ID": [1001, 1002, 1003, 1004],
    "Customer": ["Asha", "Ravi", "Neha", "Amit"],
    "Product": ["Laptop", "Phone", "Book", "Headphones"],
    "Quantity": [1, 2, 10, 2],
    "Price": [55000, 18000, 400, 2500],
    "Discount": [2000, 1000, 200, 300]
}

df = pd.DataFrame(data)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]
print("All orders:\\n", df)
print("\\nOrders above ₹5,000:\\n", df[df["Final_Amount"] > 5000])
print("\\nHighest-value order:\\n", df.loc[df["Final_Amount"].idxmax()])
print("\\nAverage order value:", df["Final_Amount"].mean())

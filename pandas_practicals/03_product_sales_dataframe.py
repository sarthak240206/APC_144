import pandas as pd

data = {
    "Product_ID": [201, 202, 203, 204],
    "Product_Name": ["Laptop", "Mouse", "Monitor", "Keyboard"],
    "Category": ["Electronics", "Accessories", "Electronics", "Accessories"],
    "Price": [55000, 700, 12000, 1500],
    "Quantity": [2, 10, 3, 5]
}

df = pd.DataFrame(data)
df["Total_Amount"] = df["Price"] * df["Quantity"]
print(df)
print("Product with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])

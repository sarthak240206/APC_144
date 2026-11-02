import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Phone", "Pen", "Desk", "Printer"],
    "Category": ["Electronics", "Electronics", "Stationery", "Furniture", "Electronics"],
    "Price": [50000, 25000, 20, 8000, 12000],
    "Quantity": [3, 4, 500, 2, 2]
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]
print(df)
print("\\nProducts with sales above ₹10,000:")
print(df[df["Total_Sales"] > 10000])
print("\\nProduct with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])
print("\\nAverage sales:", df["Total_Sales"].mean())

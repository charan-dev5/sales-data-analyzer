import pandas as pd

# Sales data
data = {
    "Product": ["Apples", "Bananas", "Mangoes", "Grapes", "Oranges"],
    "Sales": [150, 80, 200, 50, 120],
    "Price": [40, 20, 60, 80, 30]
    }

df = pd.DataFrame(data)

# Add Revenue column
df["Revenue"] = df["Sales"] * df["Price"]

# Clean data - remove anything with 0 sales
df = df[df["Sales"]>0]

print("=== SALES REPORT ===")
print(df)
print("---")
print("Total Revenue: Rs", df["Revenue"].sum())
print("Average Sales:", df["Sales"].mean())
print("Best Seller:", df.loc[df["Revenue"].idxmax(), "Product"])
print("Worst Seller:", df.loc[df["Revenue"].idxmin(), "Product"])
print("---")

# Save report to Excel
df.to_excel("sales_report.xlsx", index=False)
print("Report saved to sales_report.xlsx")

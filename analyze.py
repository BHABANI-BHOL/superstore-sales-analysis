import pandas as pd
import numpy as np

cols = ["RowID","OrderID","OrderDate","OrderPriority","OrderQty","Sales","Discount",
        "ShipMode","Profit","UnitPrice","ShippingCost","CustomerName","Province","Region",
        "CustomerSegment","ProductCategory","ProductSubCategory","ProductName",
        "ProductContainer","ProductBaseMargin","ShipDate"]

df = pd.read_csv("data/superstore_raw.csv", names=cols, header=None, engine="python", on_bad_lines="skip")

# Clean
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
df["OrderQty"] = pd.to_numeric(df["OrderQty"], errors="coerce")
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
df = df.dropna(subset=["Sales","Profit","OrderDate","Region","ProductCategory"])
df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)

print("Rows after cleaning:", len(df))
print("Date range:", df["OrderDate"].min(), "to", df["OrderDate"].max())
print("Total Sales: $%.2f" % df["Sales"].sum())
print("Total Profit: $%.2f" % df["Profit"].sum())
print("Overall profit margin: %.2f%%" % (100*df["Profit"].sum()/df["Sales"].sum()))
print()

region = df.groupby("Region").agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Orders=("OrderID","nunique")).sort_values("Sales", ascending=False)
region["Margin%"] = (region["Profit"]/region["Sales"]*100).round(2)
print("=== By Region ===")
print(region)
print()

cat = df.groupby("ProductCategory").agg(Sales=("Sales","sum"), Profit=("Profit","sum")).sort_values("Sales", ascending=False)
cat["Margin%"] = (cat["Profit"]/cat["Sales"]*100).round(2)
print("=== By Category ===")
print(cat)
print()

subcat = df.groupby("ProductSubCategory").agg(Sales=("Sales","sum"), Profit=("Profit","sum")).sort_values("Profit")
print("=== Least profitable sub-categories (top 5 loss-makers) ===")
print(subcat.head(5))
print()
print("=== Most profitable sub-categories (top 5) ===")
print(subcat.sort_values("Profit", ascending=False).head(5))
print()

yearly = df.groupby("Year").agg(Sales=("Sales","sum"), Profit=("Profit","sum"))
print("=== By Year ===")
print(yearly)
print()

segment = df.groupby("CustomerSegment").agg(Sales=("Sales","sum"), Profit=("Profit","sum")).sort_values("Sales", ascending=False)
print("=== By Segment ===")
print(segment)

df.to_csv("superstore_clean.csv", index=False)

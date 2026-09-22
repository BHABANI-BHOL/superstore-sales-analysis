import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("superstore_clean.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

plt.style.use("seaborn-v0_8-whitegrid")

# 1. Monthly sales trend
monthly = df.groupby(df["OrderDate"].dt.to_period("M"))["Sales"].sum()
fig, ax = plt.subplots(figsize=(10, 4.5))
monthly.plot(ax=ax, color="#2F5597", linewidth=1.5)
ax.set_title("Monthly Sales Trend, 2009-2012", fontsize=13, fontweight="bold")
ax.set_xlabel("")
ax.set_ylabel("Sales (USD)")
fig.tight_layout()
fig.savefig("chart_monthly_trend.png", dpi=150)
plt.close(fig)

# 2. Profit by sub-category (top/bottom performers)
subcat = df.groupby("ProductSubCategory")["Profit"].sum().sort_values()
worst = subcat.head(5)
best = subcat.tail(5)
combined = pd.concat([worst, best])
fig, ax = plt.subplots(figsize=(9, 5))
colors = ["#C0504D" if v < 0 else "#4F81BD" for v in combined.values]
combined.plot(kind="barh", ax=ax, color=colors)
ax.set_title("Least & Most Profitable Sub-Categories", fontsize=13, fontweight="bold")
ax.set_xlabel("Total Profit (USD)")
fig.tight_layout()
fig.savefig("chart_subcategory_profit.png", dpi=150)
plt.close(fig)

# 3. Region margin comparison
region = df.groupby("Region").agg(Sales=("Sales","sum"), Profit=("Profit","sum"))
region["Margin"] = region["Profit"] / region["Sales"] * 100
region = region.sort_values("Margin")
fig, ax = plt.subplots(figsize=(9, 4.5))
region["Margin"].plot(kind="bar", ax=ax, color="#4F81BD")
ax.set_title("Profit Margin % by Region", fontsize=13, fontweight="bold")
ax.set_ylabel("Margin %")
ax.set_xlabel("")
plt.xticks(rotation=30, ha="right")
fig.tight_layout()
fig.savefig("chart_region_margin.png", dpi=150)
plt.close(fig)

print("Charts saved")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

total_sales = df["Sales"].sum()
total_revenue = df["Revenue"].sum()

print("Total Sales:", total_sales)
print("Total Revenue:", total_revenue)

sales_by_region = df.groupby("Region")["Revenue"].sum()

plt.figure(figsize=(8,5))
sales_by_region.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("dashboard_output.png")

plt.show()
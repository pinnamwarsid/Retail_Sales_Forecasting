import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_sales_data.csv")

# Sales Trends Over Time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df.groupby('Order Date')['Sales'].sum().reset_index(), x='Order Date', y='Sales')
plt.title("Daily Sales Over Time")
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
plt.savefig("reports/sales_trends.png")  # Save the plot as an image
plt.show()

# Profit Margin Distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['Profit Margin'], bins=30, kde=True)
plt.title("Profit Margin Distribution")
plt.xlabel("Profit Margin")
plt.ylabel("Frequency")
plt.savefig("reports/profit_margin_distribution.png")  # Save the plot as an image
plt.show()

# Sales by Region
plt.figure(figsize=(10, 6))
sns.barplot(data=df.groupby('Region')['Sales'].sum().reset_index(), x='Region', y='Sales')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.savefig("reports/sales_by_region.png")  # Save the plot as an image
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\harsh\OneDrive\Desktop\only hars\Task1_cleaned.csv")
# Convert Purchase_Date to datetime
df["Purchase_Date"] = pd.to_datetime(
    df["Purchase_Date"],
    format="%d-%m-%Y"
)  
print("Dataset loaded successfully!")
print(df.head())
print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

#BAR CHART - CITY-WISE SALES
city_sales = df.groupby("City")["Purchase_Amount"].sum()
plt.figure(figsize=(8, 5))
plt.bar(city_sales.index, city_sales.values)
plt.title("Total Purchase Amount by City")
plt.xlabel("City")
plt.ylabel("Total Purchase Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#LINE CHART - PURCHASE TREND
daily_sales = (
    df.groupby("Purchase_Date")["Purchase_Amount"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(10, 5))

plt.plot(
    daily_sales.index,
    daily_sales.values,
    marker="o",
    label="Purchase Amount"
)

plt.title("Purchase Amount Trend Over Time")
plt.xlabel("Purchase Date")
plt.ylabel("Purchase Amount")
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()

#PIE CHART - PAYMENT METHOD
payment_counts = df["Payment_Method"].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Payment Method Distribution")
plt.show()

#HISTOGRAM - AGE DISTRIBUTION
plt.figure(figsize=(8, 5))
plt.hist(
    df["Age"],
    bins=8,
    edgecolor="black"
)

plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

#SCATTER PLOT - AGE VS PURCHASE
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Age"],
    df["Purchase_Amount"],
    alpha=0.7
)

plt.title("Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Purchase Amount")
plt.tight_layout()
plt.show()

#AVERAGE PURCHASE BY CITY
average_city_purchase = (
    df.groupby("City")["Purchase_Amount"]
    .mean()
    .sort_values(ascending=False)
)
plt.figure(figsize=(8, 5))
plt.bar(
    average_city_purchase.index,
    average_city_purchase.values
)

plt.title("Average Purchase Amount by City")
plt.xlabel("City")
plt.ylabel("Average Purchase Amount")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

#BUSINESS INSIGHTS
average_purchase = df["Purchase_Amount"].mean()
average_age = df["Age"].mean()

highest_sales_city = (
    df.groupby("City")["Purchase_Amount"]
    .sum()
    .idxmax()
)

most_used_payment = (
    df["Payment_Method"]
    .value_counts()
    .idxmax()
)

highest_purchase = df["Purchase_Amount"].max()
lowest_purchase = df["Purchase_Amount"].min()


print("\n==========================================")
print("          BUSINESS INSIGHTS")
print("==========================================")

print(
    "Average Customer Age:",
    round(average_age, 2)
)

print(
    "Average Purchase Amount:",
    round(average_purchase, 2)
)

print(
    "City with Highest Total Sales:",
    highest_sales_city
)

print(
    "Most Used Payment Method:",
    most_used_payment
)

print(
    "Highest Purchase Amount:",
    highest_purchase
)

print(
    "Lowest Purchase Amount:",
    lowest_purchase
)

#CREATE COMPLETE VISUALIZATION DASHBOARD
fig, axes = plt.subplots(2, 3, figsize=(16, 9))

# Chart 1 - City Sales
axes[0, 0].bar(
    city_sales.index,
    city_sales.values
)

axes[0, 0].set_title("City-wise Sales")
axes[0, 0].set_xlabel("City")
axes[0, 0].set_ylabel("Total Purchase")
axes[0, 0].tick_params(axis="x", rotation=45)

# Chart 2 - Purchase Trend
axes[0, 1].plot(
    daily_sales.index,
    daily_sales.values,
    marker="o",
    label="Sales"
)

axes[0, 1].set_title("Purchase Trend")
axes[0, 1].set_xlabel("Date")
axes[0, 1].set_ylabel("Purchase Amount")
axes[0, 1].tick_params(axis="x", rotation=45)
axes[0, 1].legend()

# Chart 3 - Payment Method
axes[0, 2].pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

axes[0, 2].set_title("Payment Method Distribution")

# Chart 4 - Age Distribution
axes[1, 0].hist(
    df["Age"],
    bins=8,
    edgecolor="black"
)

axes[1, 0].set_title("Age Distribution")
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_ylabel("Number of Customers")

# Chart 5 - Age vs Purchase
axes[1, 1].scatter(
    df["Age"],
    df["Purchase_Amount"],
    alpha=0.7
)

axes[1, 1].set_title("Age vs Purchase Amount")
axes[1, 1].set_xlabel("Age")
axes[1, 1].set_ylabel("Purchase Amount")

# Chart 6 - Average Purchase by City
axes[1, 2].bar(
    average_city_purchase.index,
    average_city_purchase.values
)

axes[1, 2].set_title("Average Purchase by City")
axes[1, 2].set_xlabel("City")
axes[1, 2].set_ylabel("Average Purchase")
axes[1, 2].tick_params(axis="x", rotation=45)

# Dashboard Title
fig.suptitle(
    "Customer Purchase Data Visualization Dashboard",
    fontsize=18
)

plt.tight_layout()

# Save dashboard as image
plt.savefig(
    "customer_purchase_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

#SAVE FINAL VISUALIZATION DATA
city_sales.to_csv("city_sales_summary.csv")

payment_counts.to_csv("payment_method_summary.csv")

average_city_purchase.to_csv(
    "average_purchase_by_city.csv"
)

print("\n==========================================")
print("Task 3 completed successfully!")
print("Dashboard saved as customer_purchase_dashboard.png")
print("==========================================")

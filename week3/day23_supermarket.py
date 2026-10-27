import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", context="notebook", palette="colorblind")

url="https://raw.githubusercontent.com/plotly/datasets/master/supermarket_Sales.csv"
df=pd.read_csv(url)

print(f"Shape: {df.shape}")
print(f"Column: {df.columns.tolist()}")
print(f"\nDtypes:\n {df.dtypes}")
print(f"\nMissing:\n {df.isna().sum()}")
print(f"\nDuplicates: {df.duplicated().sum()}")
print(f"\nHead: {df.head()}")

df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y",errors="coerce")
df["datetime"] = pd.to_datetime(
    df["date"].astype(str)+" "+df["time"].astype(str),
    errors="coerce"

)

df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month
df["month_name"] = df["datetime"].dt.month_name()
df["day_name"] = df["datetime"].dt.day_name()
df["hour"] = df["datetime"].dt.hour

def time_slot(hour):
    if hour < 12: return "Morning"
    if hour < 17: return "Afternoon"
    return "Evening"

df["time_slot"] = df["hour"].apply(time_slot)

df["product_line"] = df["product_line"].str.strip().str.title()
df["gender"] = df["gender"].str.strip().str.title()
df["payment"] = df["payment"].str.strip()
df["customer_type"] = df["customer_type"].str.strip()

print(f"Shape: {df.shape}")
print(f"\nDate range: {df['datetime'].min()} to {df['datetime'].max()}")
print(f"\nNew columns: {[c for c in df.columns if c not in ['invoice_id', 'branch', 'city', 'customer_type',
        'gender', 'product_line', 'unit_price', 'quantity', 'tax_5%', 'total', 'date', 'time', 'payment',
        'cost_of_goods_sold', 'gross_margin_percentage', 'gross_income', 'rating']]}")
print(f"\nDtypes:\n{df.dtypes}")
print(f"\nMissing:\n{df.isna().sum()}")

total_customers = df["invoice_id"].nunique()
print(f"Total Transactions: {total_customers}")

gender_counts = df["gender"].value_counts()
print(f"\nGender distribution:\n{gender_counts}")
print(f"\nPercent:\n{(gender_counts/len(df)*100).round(1)}")

ct = df["customer_type"].value_counts()
print(f"\nCustomer type:\n{ct}")
print(f"\nAvg rating by customer type:\n{df.groupby('customer_type')['customer_stratification_rating'].mean().round(2)}")

revenue_by_product = (
    df.groupby("product_line")["total"]
    .sum()
    .sort_values(ascending=False)
)
print(f"\nRevenue by product line:\n{revenue_by_product.round(2)}")
print(f"\nAvg rating by product line:\n{df.groupby('product_line')
    ['customer_stratification_rating'].mean().round(2).sort_values(ascending=False)}")
print(
    f"\nTotal quantity by product:\n{df.groupby('product_line')['quantity'].sum()
    .sort_values(ascending=False)}"
)

pivot_pg = df.pivot_table(
    values="total",
    index="product_line",
    columns="gender",
    aggfunc="sum"
).round(2)

print(f"\nRevenue by product x gender:\n{pivot_pg}")

revenue_by_day = df.groupby("day_name")["total"].sum().reindex(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
)
print(f"\nRevenue by day:\n{revenue_by_day.round(2)}")

revenue_by_hour = df.groupby("hour")["total"].sum()
print(f"\nRevenue by hour:\n{revenue_by_hour.round(2)}")

revenue_by_slot = df.groupby("time_slot")["total"].sum().sort_values(ascending=False)
print(f"\nRevenue by time slot:\n{revenue_by_slot.round(2)}")

revenue_by_month = df.groupby("month_name")["total"].sum().reindex([
    "January", "February", "March"]
 )
print(f"\nrevenue by month:\n{revenue_by_month.round(2)}")

revenue_by_branch = df.groupby("branch")["total"].sum().round(2).sort_values(ascending=False)
print(f"\nRevenue by branch:\n{revenue_by_branch}")

revenue_by_city = df.groupby("city")["total"].sum().round(2).sort_values(ascending=False)
print(f"\nRevenue by city:\n{revenue_by_city}")

pay = df["payment"].value_counts()
print(f"\nPayment method:\n{pay}")
print(f"\nPercent:\n{(pay/len(df)*100).round(1)}")

avg_pay_bp = df.groupby("payment")["total"].mean().round(2)
print(f"\nAvg spend by payment:\n{avg_pay_bp}")

#fig, axes = plt.subplots(2,2,figsize=(12,6))
fig, axes = plt.subplots(2,3,figsize=(20,10))
fig.suptitle("Supermarket Sales Analysis - Q1 2019", fontsize=20, fontweight="bold", y=1.01)
sns.barplot(
    x=revenue_by_product.values,
    y=revenue_by_product.index,
    ax=axes[0,0],
    palette="Blues_r"
)
axes[0,0].set_title("Revenue by Product Line", fontsize=14)
axes[0,0].set_xlabel("Revenue ($)")
axes[0,0].set_ylabel("")

sns.barplot(
    x=revenue_by_day.index,
    y=revenue_by_day.values,
    ax=axes[0,1],
    palette="Oranges"
)
axes[0,1].set_title("Revenue by Day of Week", fontsize=14),
axes[0,1].set_xlabel("")
axes[0,1].set_ylabel("Revenue ($)")
axes[0,1].tick_params(axis="x", rotation=45)

sns.lineplot(
    x=revenue_by_hour.index,
    y=revenue_by_hour.values,
    marker="o",
    ax=axes[0,2],
    color="steelblue"
)
axes[0,2].set_title("Revenue by Hour", fontsize=14)
axes[0,2].set_xlabel("Hour"),
axes[0,2].set_ylabel("Revenue ($)")

axes[1,0].pie(
    gender_counts.values,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    colors=["#7fb3d5", "#f1948a"],
    startangle=90
)
axes[1,0].set_title("Customer Gender Distribution", fontsize=14)

sns.heatmap(
    pivot_pg,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu",
    ax=axes[1,1]
)
axes[1,1].set_title("Revenue By Product x Gender", fontsize=14)
axes[1,1].set_xlabel("Gender")
axes[1,1].set_ylabel("Product Line")

sns.boxplot(
    data=df,
    x="customer_type",
    y="customer_stratification_rating",
    ax=axes[1,2],
    palette="Set2"
)
axes[1,2].set_title("Ratings by Customer Type", fontsize=14)
axes[1,2].set_xlabel("Customer Type")
axes[1,2].set_ylabel("Rating (1-10)")

plt.tight_layout()
fig.savefig("sales_dashboard.png", dpi=300, bbox_inches="tight")
plt.show()


print("=" * 60)
print("KEY INSIGHTS")
print("=" * 60)

print(f"""
1. TOP PRODUCT: {revenue_by_product.idxmax()} generated ${revenue_by_product.max():,.0f}
   ({(revenue_by_product.max()/revenue_by_product.sum()*100):.1f}% of total revenue)

2. BEST DAY: {revenue_by_day.idxmax()} with ${revenue_by_day.max():,.0f} in revenue

3. PEAK HOUR: {revenue_by_hour.idxmax()}:00 with ${revenue_by_hour.max():,.0f}

4. GENDER SPLIT: {gender_counts.index[0]} = {gender_counts.iloc[0]} transactions
({gender_counts.iloc[0]/len(df)*100:.1f}%)
{gender_counts.index[1]} = {gender_counts.iloc[1]} transactions
({gender_counts.iloc[1]/len(df)*100:.1f}%)

5. TOP BRANCH: {df.groupby('branch')['total'].sum().idxmax()} with ${df.groupby('branch')['total'].sum().max():,.0f}

6. BEST PAYMENT: {df.groupby('payment')['total'].sum().idxmax()} - ${df.groupby('payment')['total'].
sum().max():,.0f} in revenue

7. AVERAGE RATING: {df['customer_stratification_rating'].mean():.2f} / 10
   Member: {df[df['customer_type'] == 'Member']['customer_stratification_rating'].mean():.2f}
   Normal: {df[df['customer_type'] == 'Normal']['customer_stratification_rating'].mean():.2f}
""")

with open("insights_summary.txt", "w") as f:
    f.write("SUPERMARKET SALES - Q1 2019\n")
    f.write("=" * 40 + "\n\n")
    f.write(f"Total transactions: {len(df)}\n")
    f.write(f"Total revenue: ${df['total'].sum():,.0f}\n")
    f.write(f"Average transaction: {df['total'].mean():.2f}\n")
    f.write(f"Average rating  : {df['customer_stratification_rating'].mean():.2f}/10\n\n")
    f.write(f"Top product: {revenue_by_product.idxmax()}\n")
    f.write(f"Top branch: {df.groupby('branch')['total'].sum().idxmax()}\n")
    f.write(f"Top day: {revenue_by_day.idxmax()}\n")



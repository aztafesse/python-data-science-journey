import numpy as np

# Step 1 - Set up the data model
rng = np.random.default_rng(seed=42)

# Dimensions
n_stores = 500
n_regions = 4
n_products = 5
n_months = 12

# each store belongs to one rgion (roughly equal)
region_labels = rng.integers(0,n_regions,n_stores)
regions = ["North", "South", "East", "West"]

# products
products = ["Electronics", "Clothing", "Groceries", "Home", "Sports"]

# Base sales per store: mean $100k/month, std $25k
base_sales = rng.normal(100_000,25_000,n_stores)

# Each store has a product preference: some stores sell more of certain products
# Shape: (n_stores, n_products) - multiplier per product store
product_bias = rng.uniform(0.7, 1.3, (n_stores, n_products))


# Seasonal parttern: peaks in Nov/Dec (holidays), dip in Jan/Feb
# Shape: (n_months,) - multiplier per month
seasonality = np.array([0.85, 0.80, 0.95, 1.00, 1.05, 1.00,
                        0.95, 1.00, 1.05, 1.10, 1.25, 1.40])

# Growth trend: sales grow ~0.5% per month
growth = 1 + 0.005*np.arange(n_months)


print(f"Stores: {n_stores}, Regions: {n_regions}, products: {n_products}, Months: {n_months}")
print(f"Region distribution: {np.bincount(region_labels)}")

# Step 2 - Generate the Full sales Array
# Shape: (n_stores, n_prducts, n_months)
# Each cell = sales in dollars

# Combine all effects via  broadcasting
# base_sales: (50,)
# product bias: (50,5)
# seasonality: (12,)
# growth: (12,)

# Step by step
# 1. Base * product bias -> (50,5)
store_product_base = base_sales[:, np.newaxis] * product_bias  # (50,5)

# 2. Add month dimension: (50, 5, 1) * (12,) -> (50, 5, 12)
sales = store_product_base[:, :, np.newaxis] * seasonality[np.newaxis, np.newaxis, :]

# 3. Apply growth: (50, 5, 12) * (12,) -> broadcasts along last axis
sales = sales * growth[np.newaxis, np.newaxis, :]

# 4. Add noise (50, 5, 12) * random
sales = sales * rng.normal(1,0.1,(n_stores, n_products, n_months))

# 5. Round to nearest $100
sales = np.round(sales/100)*100

print(f"Sales array shape: {sales.shape}")
print(f"Total sales: ${sales.sum():,.0f}")
print(f"First store, First product, all months: {sales[0,0,:]}")

# Step 3 - Per-region Sales
print("\n=== Sales by Region ===")

# For each region, sum sales of stores in that region
# Shape: (n_regions, n_products, n_months)
region_sales = np.zeros((n_regions, n_products, n_months))

for r in range(n_regions):
    store_mask = region_labels ==  r
    region_sales[r] = sales[store_mask].sum(axis=0)

# Per-region total (sum over products and months)
region_totals = region_sales.sum(axis=(1,2))

for r, name in enumerate(regions):
    print(f"{name:6s}: ${region_totals[r]:,.0f}")


# print("\n=== Store Rankings ===")

#Total sales per store: Sum over products and months
store_totals = sales.sum(axis=(1,2)) 

# Top 5 and bottom 5
top5_idx = np.argsort(store_totals)[-5:][::-1]
bottom5_idx = np.argsort(store_totals)[:5]

print("Top 5 Stores:")
for idx in top5_idx:
    print(f" Store {idx:2d} (Region: {regions[region_labels[idx]]}): ${store_totals[idx]:,.0f}")
          
print("\nBottom 5 stores:")
for idx in bottom5_idx:
    print(f" Store {idx:2d} (Region: {regions[region_labels[idx]]}): ${store_totals[idx]:,.0f}")

print("\n=== Product Performance ===")    

# Total per product (sum over stores and months)
product_totals = sales.sum(axis=(0,2))

# Sort by revenue
sorted_idx = np.argsort(product_totals)[::-1]

for idx in sorted_idx:
    print(f"{products[idx]:12s}: ${product_totals[idx]:,.0f}")

print("\n=== Monthly Trend ===")

monthly_total = sales.sum(axis=(0, 1))

for m in range(n_months):
    bar = "█"*int(monthly_total[m]/100_000_000 *7)
    print(f"Month {m+1:2d}: ${monthly_total[m]:>12,.0f} {bar}")

print("\n=== Promotion Simulation ===")

clothing_idx = products.index("Clothing")
december_idx = 11

# Before
before_total = sales.sum()

# After: boost December clothing sales by 30%
new_sales = sales.copy()
new_sales[:,clothing_idx, december_idx] *= 1.30

after_total = new_sales.sum()
difference = after_total - before_total

print(f"Before promotion: ${before_total:,.0f}")
print(f"After promotion:  ${after_total:,.0f}")
print(f"Revenue increase: ${difference:,.0f} ({difference/before_total * 100:.2f}%)")

# effect on December clothing specifically
print(f"\nDecember clothing before: ${sales[:,clothing_idx,december_idx].sum():,.0f}")
print(f"December clothing after:  ${new_sales[:, clothing_idx, december_idx].sum():,.0f}")

print("=== Wriyte the Report ===")

with open("day14_sales_report.txt","w") as f:
    f.write("="*50+"\n")
    f.write("SALES PERFORMANCE REPORT\n")
    f.write("="*50+"\n\n")

    f.write(f"Stores: {n_stores}\n")
    f.write(f"Regions: {n_regions}\n")
    f.write(f"Products: {n_products}\n")
    f.write(f"Months: {n_months}\n\n")

    f.write("Total Sales: ${:,.0f}\n\n".format(sales.sum()))

    f.write("Sales by regions:\n")
    for r, name in enumerate(regions):
        f.write(f"  {name:6s}: ${region_totals[r]:>15,.0f}\n")
    f.write("\n")

    f.write("Product Performance:\n")
    for idx in sorted_idx:
        f.write(f"  {products[idx]:12s}:  ${product_totals[idx]:>15,.0f}\n")
    f.write("\n")

    f.write("Top 5 Stores:\n")
    for idx in top5_idx:
        f.write(f"  Store {idx:2d}: ${store_totals[idx]:>15,.0f}\n")
    f.write("\n")

    f.write("Monthly Totals\n")
    for m in range(n_months):
        f.write(f"  Month {m+1:2d}: $ {monthly_total[m]:,.0f}\n")
    f.write("\n")

    f.write("Promotion Impact:\n")
    f.write(f"  Before: ${before_total:,.0f}\n")
    f.write(f"  After: ${after_total:,.0f}\n")
    f.write(f"  Increase: ${difference:,.0f} ({difference/before_total * 100:.2f}%)\n")

print("\nReport saved to day14_sales_report.txt")



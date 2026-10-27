import pandas as pd
import numpy as np

# Task - 1 Convert and extract
print("\nTask - 1 Convert and extract")
df = pd.DataFrame({
    "date": ["2024-01-15", "2024-06-20", "2024-12-31", "2024-03-10"],
    "value": [100, 200, 150, 175]
})

df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["day_name"] = df["date"].dt.day_name()
df["day_of_week"] = df["date"].dt.dayofweek
df["quarter"] = df["date"].dt.quarter
print(df)
df["is_weekend"] = df["date"].dt.dayofweek >= 5
print(df)

# Task - 2 Date range
print("\nTask - 2 Date range")
df1 = pd.date_range(start="2024-01-01", end="2024-01-31")
print(df1)
df2 = pd.date_range("2024-01-01", periods=12, freq="ME")
print(df2)
df3 = pd.date_range("2024-06-01", periods=5, freq="B")
print(df3)

# Task - 3 Datetime index and slicing
print("\nTask - 3 Datetime index and slicing")
df = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=60, freq="D"),
    "sales": np.random.randint(50,200,60)
}).set_index("date")

print(df["2024-01-10":"2024-01-20"])
print(df.loc["2024-02"])
print(df.loc["2024-01-15"])
print(df[df.index.dayofweek < 5 ])

# Task - 4 Resample
print("\nTask - 4 Resample")
weekly = df.resample("W").sum()
print(weekly)
monthly = df.resample("ME").mean()
print(monthly)
monthly = df.resample("ME").agg({
    "sales": ["sum", "mean", "count"]
})
print(monthly)

# Task - 5 Rolling windows
print("\nTask - 5 Rolling windows")
df = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=30, freq="D"),
    "value": np.random.randint(50, 150, 30) 
}).set_index("date")

df["ma_7"] = df["value"].rolling(window=7).mean()
df["sum_7"] = df["value"].rolling(window=7).sum()
df["std_7"] = df["value"].rolling(window=7,min_periods=1).std()
df["daily_change"] = df["value"]-df["value"].shift(1)
df["pct_change"] = df["value"].pct_change()*100
print(df)

# Task - 6 Real dataset (airline passengers)
print("\nTask - 6 Real dataset (airline passengers)")
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df = pd.read_csv(url)
df["Month"] = pd.to_datetime(df["Month"])
df = df.set_index("Month")
df.columns = ["passengers"]

df1 = df.resample("YE").sum()
print(df1)
df2 = df.resample("YE").mean()
print(df2)
df3 = df.groupby(df.index.month)["passengers"].mean()
print(df3)
df["ma_12month"] = df["passengers"].rolling(window=12).mean()
df["yoy_pct"] = df["passengers"].pct_change(12)*100
print(df)
result = df.pivot_table(
    values="passengers",
    index=df.index.year,
    columns=df.index.month,
    aggfunc="sum"
)
print(result)

# Task - 7 Stock simulation
print("\nTask - 7 Stock simulation")
np.random.seed(42)
dates=pd.date_range("2024-01-01", periods=252, freq="B")
returns=np.random.normal(0.0005, 0.02, 252)
prices=100*np.cumprod(1+returns)

df=pd.DataFrame({"price":prices}, index=dates)

df["daily_return_pct"] = df["price"].pct_change()*100
df["ma_20"] = df["price"].rolling(window=20).mean()
df["ma_50"] = df["price"].rolling(window=50).mean()
df["volatility_20"] = df["price"].rolling(window=20).std()
df["max_20"] = df["price"].rolling(window=20).max()
df["min_20"] = df["price"].rolling(window=20).min()
result = df.resample("ME").agg({
    "price": ["min", "max", "first", "last"]
})
result = df["price"].resample("YE").agg(["sum", "first", "last"])
result["total_return"] = (result["last"]/result["first"]-1)*100
print(result)

# Task - 8 Bonus: Multi-key time analysis
print("\nTask - 8 Bonus: Multi-key time analysis")
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df = pd.read_csv(url)
df["Month"] = pd.to_datetime(df["Month"])
df = df.set_index("Month")
df.columns = ["passengers"]
result =df.groupby(df.index.month)["passengers"].mean()
print("The month with the highest average passenger is: ", result.idxmax())
result = df.groupby(df.index.year)["passengers"].sum()
print("The year with the highest total passengers is: ", result.idxmax())

yearly = df.resample("YE")["passengers"].sum()
yearly = yearly.reset_index(name="tot_pass")
yearly["yoy_growth"] = yearly["tot_pass"].pct_change()*100
#print(yearly.iloc[yearly["yoy_growth"].idxmax()]["Month"])
top_year = yearly.loc[yearly["yoy_growth"].idxmax(), "Month"]
print(f"The highest growth year is: {top_year.year}")

result = df.groupby(df.index.quarter)["passengers"].sum()
print(result)
result = df.pivot_table(
    values="passengers",
    index=df.index.quarter,
    columns=df.index.year,
    aggfunc="sum",
)
print(result)
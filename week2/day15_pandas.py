import pandas as pd
import numpy as np

# Task 1 - Create a DataFrame
data = {
    "name": ["Aziz", "Ali", "Sara", "Omar", "Layla"],
    "age": [25, 22, 24, 28, 21],
    "city": ["Dubai", "Abu Dhabi", "Sharjah", "Dubai", "Abu Dhabi"],
    "math": [88, 72, 95, 60, 80],
    "science": [90, 65, 88, 75, 82],
    "english": [78, 80, 92, 70, 85]
}
df = pd.DataFrame(data)

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())

# Task 2 - Column access
print("\n=== Task 2 - Column access ===")
print(df["name"])
print(df[["name","math"]])
print(df.head(3))
print(df.tail(2))

# Task 3 - Row access
print("\n=== Row access ===\n")
print(df.iloc[0])
print(df.loc[2])
print(df.iloc[0,3])
print(df.loc[:,"math"])

# Task 4 - Filtering
print("=== Filtering ===")
print(df)
print(df[df["math"] > 80])
print(df[df["city"] == "Dubai"])
print(df[(df["age"] > 22) & (df["science"] >80)])
print(df[df["city"].isin(["Dubai", "Sharjah"])])

# Task 5 - Aggregations
print("=== Aggregation ===")
print(f"Averages math: {df['math'].mean()}, science: {df['science'].mean()}, english: {df['english'].mean()}")
print(f"Maxes math: {df['math'].max()}, science: {df['science'].max()}, english: {df['english'].max()}")
print(f" Mins math: {df['math'].min()}. science: {df['science'].min()}, english: {df['english'].min()}")
print(df["city"].value_counts())

# Task 6 - Adding columns
print("=== Adding columns ===")
df["total"] = df["math"]+ df["science"]+ df["english"]
df["average"] = df["total"]/3
df["passed_all"] = (df["math"]>= 60) & (df["science"]>=60) & (df["english"]>=60)

# Task 7 - Load a real CSV
print("=== Load a real CSV ===")
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
print(df.head())
print(df.info())
print(df.describe())
print(df["total_bill"].mean())
print(df["tip"].mean())
print(df[df["total_bill"]>30])
print(df["day"].value_counts())

# Task 8 - Bonus: Mini analysis
print("=== Bonus: Mini analysis ===")
average_tip= df.groupby("day")["tip"].mean()
print(average_tip)

time_avg_tip = df.groupby("time")["tip"].mean()
print(time_avg_tip)

smokers_count = df["smoker"].value_counts()
print(smokers_count)

df["avg_tip"] = (df["tip"]/df["total_bill"])*100
print(f"Average tip percentage: {df['avg_tip'].mean():.2f} %")
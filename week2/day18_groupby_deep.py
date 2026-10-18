import pandas as pd
import numpy as np

# Task - 1 Basic aggregation
print("\nTask - 1 Basic aggregation")
df = pd.DataFrame({
    "dept": ["HR", "IT", "HR", "IT", "Sales", "Sales", "HR"],
    "name": ["A","B", "C","D", "E", "F", "G"],
    "salary": [50_000, 70_000, 55_000, 80_000, 60_000, 65_000, 48_000],
    "age": [30, 28, 35, 32, 40, 27, 45]
})
df.groupby("dept")["salary"].mean()
df.groupby("dept")["salary"].max()
df.groupby("dept")["salary"].min()
df.groupby("dept")["salary"].count()
df.groupby("dept")["age"].mean()

df.groupby("dept").agg({
    "salary": ["mean", "max", "min", "count"],
    "age": ["mean"]
})

# Task - 2 Named aggregations
print("\nTask - 2 Named aggregations")
print(df.groupby("dept").agg(
    avg_salary=("salary", "mean"),
    max_salary=("salary", "max"),
    min_salary=("salary","min"),
    count_of_salary=("salary","count"),
    avg_age=("age", "mean")
))

# Task - 3 Multi-key groupby
print("\nTask 3 Multi-key groupby")
def age_cat(age):
    if age<30: return "young"
    if age<40: return "mid"
    return "senior"

df["age_bin"]=df["age"].apply(age_cat)
result = df.groupby(["dept","age_bin"])["salary"].mean()
print(result)
result=result.reset_index()
print(result)

# Task - 4 Transform
print("\nTask - 4 Transform")
df["dept_avg_salary"] = df.groupby("dept")["salary"].transform("mean")
print(df)
df["salary_pct_of_dept"] = df["salary"]/df["dept_avg_salary"]*100
print(df)
df["rank_in_dept"] = df.groupby("dept")["salary"].rank(ascending=False)
print(df)

# Task - 5 Filter
print("\nTask - 5 Filter")
df1 = df.groupby("dept").filter(lambda g: len(g)>2)
df1 = df1.groupby("dept").filter(lambda g: g["salary"].mean()>55_000)
df1 = df1.groupby("dept").filter(lambda g: g["salary"].max()>70_000)
print(df1)

# Task - 6 Apply
print("\nTask - 6 Apply")
df2 = df.groupby("dept").apply(lambda g: g["salary"].max()-g["salary"].min())
print(df2)

def top_earner(g):
    return g.nlargest(1, "salary")

df3 = df.groupby("dept").apply(top_earner)
print(df3)

# Task - 5 Pivot table
print("\nTask - 5 Pivot table")
df2 = pd.DataFrame({
    "dept": ["HR", "HR", "IT", "IT", "Sales", "Sales"],
    "gender": ["F", "M", "F", "M", "F", "M"],
    "salary": [50_000, 55_000, 70_000, 80_000, 60_000, 65_000]
})

result = df2.pivot_table(
    values="salary",
    index="dept",
    columns="gender",
    aggfunc="mean"
)
print(result)

result = df2.pivot_table(
    values="salary",
    index="dept",
    columns="gender",
    aggfunc="mean",
    margins=True
)
print(result)

result = df2.pivot_table(
    values="salary",
    index="dept",
    columns="gender",
    aggfunc=["mean", "max"]
)
print(result)

# Task - 8 Crosstab
print("\nTask - 8 Crosstab")
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
tips = pd.read_csv(url)
result = pd.crosstab(tips["day"], tips["time"])
print(result)
result = pd.crosstab(tips["day"], tips["time"],margins=True)
print(result)
result = pd.crosstab(tips["smoker"], tips["sex"], margins=True)
print(result)

# Task - 9 Real analytics
print("\nTask - 9 Real analytics")
tips["tip_pct"] = tips["tip"]/tips["total_bill"] * 100
result = tips.groupby("day").agg(
    avg_tip = ("tip", "mean"),
    avg_bill = ("total_bill", "mean"),
    avg_pct = ("tip_pct", "mean"),
    n_meals = ("total_bill","count")
)
print(result)
result  = tips.pivot_table(
    values="tip_pct",
    index="day",
    columns="smoker",
    aggfunc="mean",
)
print(result)

result = tips.groupby(["day", "smoker"])["tip_pct"].mean()
print(result)

tips["bill_vs_day_avg"] = tips["total_bill"]-tips.groupby("day")["total_bill"].transform("mean")

tips = tips.groupby("day").filter(lambda g: g["total_bill"].mean() > 18)
print(tips[["day", "total_bill", "bill_vs_day_avg"]].head())

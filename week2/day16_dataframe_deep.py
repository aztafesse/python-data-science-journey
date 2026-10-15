import numpy as np
import pandas as pd

# Task 1 - Set and reset index
print("=== Task 1 - Set and reset index ===")
df = pd.DataFrame({
    "id": [101, 102, 103, 104],
    "name": ["Aziz", "Ali", "Sara", "Omar"],
    "age": [25, 22, 24, 28],
    "score": [88, 92, 79, 95],
})

df = df.set_index("id")
print(df)
print(df.loc[103])
df = df.reset_index()

# Task 2 - Sorting
print("\n=== Task 2 ===")
df = df.sort_values("score", ascending = True)
df = df.sort_values("score", ascending = False)
df = df.sort_values(["age", "score"], ascending = [True, False])
print(df)

# Task 3 - Missing data
print("\n=== Task 3 - Missing data ===")
df = pd.DataFrame({
    "name": ["Aziz", "Ali", "Sara", "Omar", "Layla"],
    "age": [25, np.nan, 24, 28, 21],
    "score":[88, 92, np.nan, 95, 79],
    "city": ["Dubai", "Abu Dhabi", None, "Dubai", "Sharjah"]
})

print(df.isna().sum())
print(df.isna().sum()/len(df)*100)
print(df.dropna())
print(df.fillna(df["age"].mean()))
print(df.fillna({"score": 0}))
print(df.fillna({"city":"Unknown"}))

# Task 4 - Renaming & reordering
print("=== Tast 4 - Renaming & reordering ===\n")
df = df.rename(columns={"name": "student_name", "score": "exam_score"})
df = df[["age", "city", "exam_score", "student_name"]]
df.columns = df.columns.str.lower()

# Task - 5 Apply functions
print("\n=== Task 5 - Apply functions ===")
df = pd.DataFrame({
    "name": ["Aziz", "Ali", "Sara", "Omar", "Layla"],
    "age": [25, np.nan, 24, 28, 21],
    "score":[88, 92, np.nan, 95, 79],
    "city": ["Dubai", "Abu Dhabi", None, "Dubai", "Sharjah"]
})

def letter_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    return "F"

df["grade"] = df["score"].apply(letter_grade)
df["name_length"] = df["name"].apply(lambda x: len(x))
df["summary"] = df.apply(lambda row: f"{row['name']} ({row['city']}) scored {row['score']}", axis = 1)
print(df)

df["name_length"] = df["name"].str.len()

# Task 6 - Groupby
print("\n=== Task 6 - Groupby ===")

df = pd.DataFrame({
    "dept": ["HR", "IT", "HR", "IT", "Sales", "Sales"],
    "name": ["A", "B", "C", "D", "E", "F"],
    "salary": [50_000, 70_000, 55_000, 80_000, 60_000, 65_000],
    "age": [30, 28, 35, 32, 40, 27]
})

print(df.groupby("dept").agg({
    "salary": ["mean", "sum", "max", "min", "count"],
    "age" : ["max", "min"]
}))

# Task 7 - Real data (tips)
print("\n=== Task 7 - Real data (tips) ===")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
print(df.sort_values("total_bill", ascending = False).head(10))
print(df.groupby("day")["tip"].mean())
print(df.groupby("time")["total_bill"].mean())
print(df.groupby(["day", "time"])["tip"].mean())
df["tip_pct"] = df["tip"]/df["total_bill"] * 100
print(df.groupby("smoker")["tip_pct"].mean())

# Task 8 - Bonus: Comprehensive analysis
print("\n=== Task 8 - Bonus: Comprehensive analysis ===")

df["week"] = np.where(df["day"].isin(["Thur", "Fri"]), "Weekdays", "Weekends")

print(df.groupby("week")["tip"].mean())
print(df.groupby("day")["total_bill"].mean())
print(df.groupby("smoker")["tip_pct"].mean())
def bill_category(total_bill):
    if total_bill < 15 : return "small"
    if total_bill < 30 : return "medium"
    return "large"

df["bill_size"] = df["total_bill"].apply(bill_category)
print(df.groupby("bill_size")["tip"].mean())


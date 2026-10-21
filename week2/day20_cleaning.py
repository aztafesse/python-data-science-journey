import pandas as pd
import numpy as np

# Task - 1 Build the messy dataset
print("\nTask - 1 Build the messy dataset")
df = pd.DataFrame({
    "Name": ["  Aziz", "ali", "SARA", " Omar", "Layla", "ali", "Sara"],
    "Age": ["25", "22", "twenty-four", "28", "21", None, "24"],
    "Score": ["88", "92.5", "n/a", "95", "79", "92.5", "79"],
    "City": ["Dubai", "abu dhabi", "Sharjah", "DUBAI", "dubai", "abu dhabi", "Sharjah"],
    "Date": ["2024-01-15", "2024-02-20", "not a date", "2024-03-10",
             "2024-4-05","2024-05-12", "2024-06-30"]
})

print(df.head())
print(df.dtypes)
print(df.isna().sum())
print(df.shape)

# Task - 2 Clean column names
print("\nTask - 2 Clean column names")
df.columns = (
    df.columns.str.strip().str.lower().str.replace(" ", "_")
)
print(df.columns)

# Task - 3 Fix types
print("\nTask - 3 Fix types")
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")

print(df.dtypes)
print(df.isna().sum())

# Task - 4 Clean strings
print("\nTask - 4 Clean strings")
df["name"] = df["name"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.lower().str.title()
print(df[["name", "city"]])

# Task - 5 Handle missing values
print("\nTask - 5 Handle missing values")
df["age"] = df["age"].fillna(df["age"].median())
df["score"] = df["score"].fillna(df["score"].mean().round(2))
df["city"] = df["city"].fillna("Unknown")
df=df.dropna(subset=["date"])
print(df.isna().sum())

# Task - 6 Deduplicate
print("\nTask - 6 Deduplicate")
dupes_before = df.duplicated().sum()
df1 = df.drop_duplicates(keep="first")
rows_removed = len(df)-len(df1)
print(f"Duplicates found: {dupes_before}")
print(f"number of rows removed is: {rows_removed}")

# Task - 7 Outliers
print("\nTask - 7 Outliers")
df2 = pd.DataFrame({"value": [10, 12, 11, 13, 12, 11, 10, 100, 12, 11, 13, -5, 12]})
q1 = df2["value"].quantile(0.25)
q3 = df2["value"].quantile(0.75)
iqr = q3-q1
print(f"q1 = {q1}, q3 = {q3}, IQR = {iqr}")
lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr
outliers = df2[(df2["value"] < lower) | (df2["value"] > upper)]
print(f"outliers are:\n {outliers}")
shape_before = df2.shape
df2=df2[(df2["value"] >= lower) & (df2["value"] <= upper)]
shape_after = df2.shape
print(f"Before shape: {shape_before}, After shape: {shape_after}")

# Task - 8 Binning
print("\nTask - 8 Binning")
print(df1)
df1["age_group"] = pd.cut(
    df1["age"],
    bins = [0, 18, 30, 50, 100],
    labels=["child", "young", "middle", "senior"]
)
print(df1["age_group"].value_counts())
df1["score_quartile"] = pd.qcut(
    df1["score"],
    q=4,
    labels=["Q1", "Q2", "Q3", "Q4"]
)
print(df1["score_quartile"].value_counts())

# Task - 9 Save
print("\nTask - 9 Save")
df1.to_csv("cleaned_data.csv", index=False)
df4 = pd.read_csv("cleaned_data.csv", parse_dates=["date"])
print(df4.dtypes)
print(df4.head())

# Task - 10 Pipeline
print("\nTask - 10 Pipeline")
df = pd.DataFrame({
    "Name": ["  Aziz", "ali", "SARA", " Omar", "Layla", "ali", "Sara"],
    "Age": ["25", "22", "twenty-four", "28", "21", None, "24"],
    "Score": ["88", "92.5", "n/a", "95", "79", "92.5", "79"],
    "City": ["Dubai", "abu dhabi", "Sharjah", "DUBAI", "dubai", "abu dhabi", "Sharjah"],
    "Date": ["2024-01-15", "2024-02-20", "not a date", "2024-03-10",
             "2024-4-05","2024-05-12", "2024-06-30"]
})

def clean_data(df):
    df = df.copy()
    df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["name"] = df["name"].str.strip().str.title()
    df["city"] = df["city"].str.strip().str.lower().str.title()
    df["age"] = df["age"].fillna(df["age"].median())
    df["score"] = df["score"].fillna(df["score"].mean().round(2))
    df["city"] = df["city"].fillna("Unknown")
    df = df.dropna(subset=["date"])
    df = df.drop_duplicates()
    return df

df_clean = clean_data(df)
df_clean.to_csv("students_clean.csv", index=False)

print(f"Shape: {df_clean.shape}")
print(f"Types: {df_clean.dtypes}")
print(f"Missing values: {df_clean.isna().sum()}")

# Task - 11 Bonus: Messy real data (Titanic)
print("\nTask - 11 Bonus: Messy real data (Titanic)")
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
print(df.info())
print(df.isna().sum())
print(df.duplicated().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df=df.drop(columns=["Cabin"])

print(df["Sex"].value_counts())
print(df["Embarked"].value_counts())
q1 = df["Fare"].quantile(0.25)
q3 = df["Fare"].quantile(0.75)
iqr = q3-q1
lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr
outliers = df[(df["Fare"] < lower) | (df["Fare"] > upper)]
df = df[(df["Fare"] >= lower) & (df["Fare"] <= upper)]
print(outliers.shape)
df.to_csv("titanic_clean.csv", index=False)

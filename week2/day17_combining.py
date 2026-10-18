import pandas as pd
import numpy as np

# Task - 1 Vertical concat
print("Task - 1 Vertical concat")
q1 = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar"],
    "sales": [100, 150, 200]
})
q2 = pd.DataFrame({
    "month": ["Apr", "May", "Jun"],
    "sales": [220, 180, 240]
})
q_merged = pd.concat([q1, q2], ignore_index = True)
print(q_merged)

# Task - 2 Horizontal concat
print("\nTask - 2 Horizontal concat")
left = pd.DataFrame({"name": ["Aziz", "Ali", "Sara"]})
right = pd.DataFrame({"score": [88, 92, 79]})

merged = pd.concat([left, right], axis = 1)
print(merged)

# Task - 3 Basic inner merge
print("\nTask - 3 Basic inner merge")
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Aziz", "Ali", "Sara", "Omar"]
})
grades = pd.DataFrame({
    "student_id": [1, 2, 2, 3, 4, 4, 4],
    "subject": ["Math", "Math", "Science", "Math", "Math", "Science", "English"],
    "score": [88, 92, 85, 79, 95, 91, 88]
})

merged = pd.merge(students, grades, on="student_id", how="inner")
print(merged) # there is 7 rows, because merge inner is on matching student_id

merged = pd.merge(students, grades, on="student_id", how="left")
print(merged) # Row count does not change

merged = pd.merge(students, grades, on="student_id", how="outer")
print(merged) # no difference

# Task 4 - Join types comparison
print("\nTask 4 - Join types comparison")
left = pd.DataFrame({"id": [1, 2, 3, 5], "A": ["a1", "a2", "a3", "a5"]})
right = pd.DataFrame({"id": [2, 3, 4, 5], "B": ["b2", "b3", "b4", "b5"]})

merged_inner = pd.merge(left, right, on="id", how="inner")
print(merged_inner) # 3 rows and no NaN
merged_left = pd.merge(left, right, on="id", how="left")
print(merged_left) # 4 rows with NaN on row 0 B column
merged_right = pd.merge(left, right, on="id", how="right")
print(merged_right) # 4 rows with NaN on row 2 A column
merged_outer = pd.merge(left, right, on="id", how="outer")
print(merged_outer) # 5 rows with NaN on row 0 column B and on row 3 column A

# Task - 5 Merge on different column names
print("\nTask - 5 Merge on different column names")
users = pd.DataFrame({"user_id": [101, 102, 103], "name": ["Aziz", "Ali", "Sara"]})
orders = pd.DataFrame({"uid": [101, 101, 103, 104], "amount": [50, 100, 75, 200]})
merged = pd.merge(users, orders, left_on="user_id", right_on="uid")
print(merged)
merged = merged.drop(columns="uid")
print(merged)

# Task - 6 Merge on multiple keys
print("\nTask - 6 Merge on multiple keys")
sales = pd.DataFrame({
    "region": ["North", "North", "South", "South"],
    "year": [2023, 2024, 2023, 2024],
    "revenue": [100, 120, 90, 110]
})
costs = pd.DataFrame({
    "region": ["North", "North", "South", "South"],
    "year": [2023, 2024, 2023, 2024],
    "cost": [60, 70, 55, 65]
})

merged = pd.merge(sales, costs, on=["region", "year"])
print(merged)
merged["profit"] = merged["revenue"]-merged["cost"]
print(merged)
merged = merged.sort_values("profit", ascending = False)
print(merged)

# Task - 7 Real world scenario (tips split)
print("\nTask - 7 Real world scenario (tips split)")
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
tips = pd.read_csv(url)

tips_a = tips.iloc[:100]
tips_b = tips.iloc[100:]

recombined = pd.concat([tips_a, tips_b], ignore_index = True)

print(recombined.shape)
print(tips.shape)
print(tips.iloc[:5])

categories = pd.DataFrame({
    "day": ["Thur", "Fri", "Sat", "Sun"],
    "is_weekend": [False, False, True, True]
})

merged = pd.merge(tips, categories, on="day")
print(merged.groupby("is_weekend")["tip"].mean())

# Task - 8 Bonus: Anti-join
print("\nTask - 8 Bonus: Anti-join")
customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4, 5],
    "name": ["A", "B", "C", "D", "E"]
})
orders = pd.DataFrame({
    "customer_id": [1, 1, 2, 3],
    "amount": [100, 200, 300, 400]
})

merged = pd.merge(customers, orders, on="customer_id", how="left", indicator=True)
no_orders = merged[merged["_merge"]=="left_only"]
print(no_orders[["customer_id", "name"]])

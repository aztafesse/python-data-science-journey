import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Task - 1 Line plot
print("\nTask - 1 Line plot")
x = np.arange(1,11)
y = x ** 2

fig, ax = plt.subplots()
ax.plot(x, y, marker="*")
ax.set_title("Line Plot")
fig.savefig("square_plot.png", dpi=300)
plt.show()

# Task - 2 Histogram
print("\nTask - 2 Histogram")
data = np.random.normal(70, 10, 1000)
fig, ax = plt.subplots()
ax.hist(data, bins=20)
ax.set_title("exam_scores")
fig.savefig("Exam Scores.png", dpi=300)
plt.show()

# Task - 3 Bar chart
print("\nTask - 3 Bar chart")
products = ["Electronics", "Clothing", "Groceries", "Home", "Sports"]
revenue = [45000, 62000, 78000, 35000, 28000]

fig, ax = plt.subplots()
ax.bar(products, revenue)
ax.set_title("Revenue per products")
ax.set_ylabel("Revenue")
#ax.set_xticklabels(products, rotation=45)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
plt.show()

# Task - 4 Scatter plot
print("\nTask - 4 Scatter plot")
tips = sns.load_dataset("tips")

fig, ax = plt.subplots()
sns.scatterplot(data=tips, x="total_bill", y="tip",hue="sex")
ax.set_title("Total bill vs tip")
ax.set_xlabel("Total_bill")
ax.set_ylabel("Tip")
plt.show()

# Task - 5 Subplots
print("\nTask - 5 Subplots")
fig, axes = plt.subplots(1,2, figsize=(12, 4))
sns.histplot(data=tips, x="total_bill", bins=20, kde=True, ax=axes[0])
axes[0].set_title("Distribution of Total Bill")
axes[0].set_xlabel("Total Bill")

sns.boxplot(data=tips,x="day", y="total_bill", ax=axes[1])
axes[1].set_title("Comparison Day vs Total bill")
axes[1].set_xlabel("Day")
axes[1].set_ylabel("Total_bill")
plt.tight_layout()
plt.show()

# Task - 6 Seaborn distributions
print("\nTask - 6 Seaborn distributions")
fig, axes = plt.subplots(1,3,figsize=(18,4))
sns.histplot(data=tips, x="tip",bins=20, kde=True, ax=axes[0])
axes[0].set_title("Tips distribution")
axes[0].set_xlabel("Tips")

sns.boxplot(data=tips, x="day", y="tip", ax=axes[1])
axes[1].set_xlabel("Day")
axes[1].set_ylabel("Tip")
axes[1].set_title("Comparison Day vs Tip")

sns.violinplot(data=tips, x="time", y="total_bill", ax=axes[2])
axes[2].set_title("Comparison Time vs Total bill")
axes[2].set_xlabel("Time")
axes[2].set_ylabel("Total Bill")

plt.tight_layout()
plt.show() # Observed on the chart 1 that the highest count of tips is around $ 2,
# on chart 2, sunday have the higher tips paid, on thurday, friday and saturday, tips are in avegare the same.
# on chart 3, observed that dinner have the highest total bill.

# Task - 7 Seaborn relationships
print("\nTask - 7 Seaborn relationship")
fig, axes = plt.subplots(1,2,figsize=(12,4))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", size="size", ax=axes[0])
axes[0].set_title("Scatter plot")
axes[0].set_xlabel("Total Bill")
axes[0].set_ylabel("Tip")

sns.regplot(data=tips, x="total_bill", y="tip", ax=axes[1])
axes[1].set_title("Regression plot")
axes[1].set_xlabel("Total bill")
axes[1].set_ylabel("Tip")
plt.tight_layout()
plt.show()

g = sns.pairplot(tips, hue="time")
g.figure.suptitle("Pair Plot", y=1.02)
plt.show() # There is a linear trend between total bill and tip

# Task - 8 Categorical
print("\nTask - 8 Categorical")
fig, axes = plt.subplots(1,3,figsize=(18,4))
sns.barplot(data=tips,x="day", y="tip", ax=axes[0])
axes[0].set_title("Bar plot Day vs Tip")
axes[0].set_xlabel("Day")
axes[0].set_ylabel("Tip")

sns.countplot(data=tips,x="day", ax=axes[1])
axes[1].set_title("Count Plot")
sns.barplot(data=tips, x="day", y="total_bill", hue="sex", ax=axes[2])
axes[2].set_title("Bar plot Day vs Total Bill")
axes[2].set_xlabel("Day")
axes[2].set_ylabel("Total Bill")

plt.tight_layout()
plt.show()

# Task - 9 Heatmap
print("\nTask - 9 Heatmap")
corr=tips.select_dtypes(include="number").corr()
fig, ax = plt.subplots(figsize=(12,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1)
ax.set_title("Correlation Matrix")
plt.show() # The two variables that are most correlated are Tips and total_bill

# Task - 10 Real dashboard
print("\nTask - 10 Real dashboard")

fig, axes = plt.subplots(2,2,figsize=(14,10))
sns.histplot(data=tips,x="total_bill", ax=axes[0,0])
axes[0,0].set_title("Histogram of Total bill")
axes[0,0].set_xlabel("Total Bill")

sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", ax=axes[0,1])
axes[0,1].set_title("Scatter plot of Total Bill vs Tip")
axes[0,1].set_xlabel("Total Bill")
axes[0,1].set_ylabel("Tip")

sns.boxplot(data=tips, x="day", y="tip", ax=axes[1,0])
axes[1,0].set_title("Box plot of Day vs Tip")
axes[1,0].set_xlabel("Day")
axes[1,0].set_ylabel("Tip")

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1, ax=axes[1,1])
axes[1,1].set_title("Heatmap of correlations")

plt.tight_layout()
fig.savefig("tips_dashboard.png", dpi=300, bbox_inches="tight")
plt.show()


# Task - 11 Bonus: Airline passengers trend
print("\nTask - 11 Bonus: Airline passengers trend")
url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df=pd.read_csv(url, parse_dates=["Month"], index_col="Month")
df.columns = ["passengers"]
#fig, ax=plt.subplots()
#ax.plot(df["Month"],df["passengers"])
#ax.set_title("#####")

df.plot(y=["passengers"])
plt.show()
df["ma_12"] = df["passengers"].rolling(window=12).mean()
df.plot(y=["passengers", "ma_12"], color=["blue", "red"], title="Airline Passengers 1949-1960")
plt.show()

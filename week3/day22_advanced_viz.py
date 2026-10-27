import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


 # Task - 1 Apply a theme
print("\nTask - 1 Apply a theme")
fig, ax = plt.subplots()
sns.set_theme(style="whitegrid", context="talk", palette="colorblind")
tips = sns.load_dataset("tips")
sns.scatterplot(data=tips,x="total_bill", y="tip", hue="time", ax=ax)
plt.show()

# Task - 2 Annotations
print("\nTask - 2 Annotations")
max_idx = tips["total_bill"].idxmax()
max_row = tips.loc[max_idx]
fig, ax = plt.subplots(figsize=(10,6))
sns.scatterplot(data=tips, x="total_bill", y="tip", ax=ax)
ax.annotate(
    f"Largest bill: ${max_row['total_bill']:.2f}",
    xy=(max_row["total_bill"],max_row["tip"]),
    xytext=(max_row["total_bill"]-15,max_row["tip"]+1),
    arrowprops=dict(arrowstyle="->", color="red", lw=1.5),
    fontsize=10,
    color="red"
)
ax.set_title("Tip vx Total Bill")
ax.axhline(y=tips["tip"].mean(), color="red", linestyle="--", label=f"Mean tip = ${tips['tip'].mean():.2f}")
ax.axvline(x=tips["total_bill"].mean(), color="green", linestyle="--", label=f"Mean total bill: ${tips['total_bill'].mean():.2f}", alpha=0.5)
ax.legend()

plt.show()

# Task - 3 Reference regions
print("\nTask - 3 Reference rgions")
fig, ax = plt.subplots(figsize=(10,6))
sns.scatterplot(data=tips, x="total_bill", y="tip", ax=ax)
ax.annotate(
    f"Largest bill: ${max_row['total_bill']:.2f}",
    xy=(max_row["total_bill"],max_row["tip"]),
    xytext=(max_row["total_bill"]-15,max_row["tip"]+1),
    arrowprops=dict(arrowstyle="->", color="red", lw=1.5),
    fontsize=10,
    color="red"
)
ax.set_title("Tip vx Total Bill")
ax.axhline(y=tips["tip"].mean(), color="red", linestyle="--", label=f"Mean tip = ${tips['tip'].mean():.2f}")
ax.axvline(x=tips["total_bill"].mean(), color="green", linestyle="--", label=f"Mean total bill: ${tips['total_bill'].mean():.2f}", alpha=0.5)
ax.axhspan(0,2, color="gray", alpha=0.7)
ax.text(40,1,"Low tips", fontsize=12, color="brown")
ax.legend()

plt.show()

# Task - 4 Dual y-axis
print("\nTask - 4 Dual y-axis")
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df = pd.read_csv(url, parse_dates=["Month"], index_col="Month")
df.columns = ["passengers"]
df["ma_12"] = df["passengers"].rolling(12).mean()
fig, ax1 = plt.subplots(figsize=(12,6))

ax1.plot(df.index, df["passengers"], color="blue", alpha=0.6, label="Monthly passengers")
ax1.set_xlabel("Date")
ax1.set_ylabel("Passengers", color = "blue")
ax1.tick_params(axis="y", color="blue")

ax2 = ax1.twinx()
ax2.plot(df.index, df["ma_12"], color="red", lw=2, label="12-month MA")
ax2.set_ylabel("12-month Moving Average", color="red")
ax2.tick_params(axis="y", color="red")

fig.suptitle("Airline Passengers with 12-Month Trend")
plt.tight_layout()
plt.show()

# Task - 5 Faceting with replot
print("\nTask - 5 Faceting with replot")
g = sns.relplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")
g.fig.suptitle(" Total Bill vs Tip by time", y=1.001)
plt.show()
g = sns.relplot(data=tips, x="total_bill",y="tip", col="time", row="smoker")
g.fig.suptitle(" Total Bill vs Tip by time", y=1.001, fontsize=12)
plt.show()

# Task - 6 FacetGrid for control
print("\nTask - 6 FaceGrid for control")
g = sns.FacetGrid(tips, col="time", row="smoker", height=4)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip", hue="sex")
g.add_legend()
g.set_axis_labels("Total Bill ($)", "Tip ($)")
g.set_titles(col_template="{col_name}-{row_name}")
g.fig.suptitle("Tips by Time and Smoking status", y=1.005, fontsize=9)
plt.show()

# Task - 7 Displot
print("\nTask - 8 Displot")
g = sns.displot(data=tips,x="tip", col="day", kde=True, height=3)
plt.show()

# Task - 8 Decluttering
print("\nTask - 8 Decluttering")

fig, ax = plt.subplots()
sns.set_theme(style="whitegrid", context="talk", palette="colorblind")
tips = sns.load_dataset("tips")
sns.scatterplot(data=tips,x="total_bill", y="tip", hue="time", ax=ax)
sns.despine()
ax.set_xlabel("Total Bill ($)", fontsize=10)
ax.set_ylabel("Tip ($)", fontsize=10)
ax.set_title("Total Bill vs Tips", fontsize=10)
plt.show()

# Task - 9 Presentation-ready figure
print("\nTask - 9 Presentation-ready figure")

sns.set_theme(style="whitegrid", context="talk", palette="colorblind")
fig, ax=plt.subplots(figsize=(10,6))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", alpha=0.7, ax=ax)
ax.set_title("Tip Increases with Bill - Regardless of Meal Time", fontweight="bold", pad=20)
ax.set_xlabel("Total Bill ($)", fontsize = 12)
ax.set_ylabel("Tip ($)", fontsize = 12)
max_idx = tips["total_bill"].idxmax()
ax.annotate(
    f"Largest bill: ${tips.loc[max_idx, 'total_bill']:.2f}",
    xy=(tips.loc[max_idx,"total_bill"], tips.loc[max_idx,"tip"]),
    xytext=(tips.loc[max_idx,"total_bill"]-8, tips.loc[max_idx,"tip"]+0.75),
    arrowprops=dict(arrowstyle="->", color="gray"), 
    fontsize=10,
    color="gray"
)

sns.despine()
plt.tight_layout()
fig.savefig("presentation_ready.png", dpi=300, bbox_inches="tight")
plt.show()

# Task - 10 Bonus:Storytelling dashboard
print("\nTask - 10 Bonus:Storytelling dashboard")

tips["tip_pct"]=tips["tip"]/tips["total_bill"]*100

fig, axes = plt.subplots(2,2,figsize=(12,6))
fig.suptitle("Tips DataSet Dashboard", fontsize=18, fontweight="bold",y=0.98)
sns.histplot(data=tips, x="total_bill",bins=30, kde=True, color="skyblue", ax=axes[0,0])
axes[0,0].set_title("Distribution of Total Bill")
axes[0,0].set_xlabel("Total Bill ($)")
sns.boxplot(data=tips, x="day", y ="tip_pct", palette="Set2", ax=axes[0,1])
axes[0,1].set_title("Tip Percentage by Day")
axes[0,1].set_xlabel("Day")
axes[0,1].set_ylabel("Tip Percentage (%)")
sns.scatterplot(data=tips, x="total_bill", y="tip", ax=axes[1,0])
axes[1,0].set_title("Bill vs Tip")
axes[1,0].set_xlabel("Total Bill ($)")
axes[1,0].set_ylabel("Tip ($)")
max_idx = tips["total_bill"].idxmax()
axes[1,0].annotate(
    f"Largest bill: ${tips.loc[max_idx, 'total_bill']:.2f}",
    xy=(tips.loc[max_idx,"total_bill"], tips.loc[max_idx,"tip"]),
    xytext=(tips.loc[max_idx,"total_bill"]-8, tips.loc[max_idx,"tip"]-0.75),
    arrowprops=dict(arrowstyle="->", color="gray"), 
    fontsize=10,
    color="gray"
)
sns.boxplot(data=tips, x="time", y="total_bill", hue="smoker", ax=axes[1,1])
axes[1,1].set_title("Total Bill by Time & Smoker")
axes[1,1].set_xlabel("Time")
axes[1,1].set_ylabel("Total Bill ($)")

plt.tight_layout()
plt.savefig("tips_story.png",dpi =300, bbox_inches="tight")
plt.show()

# Task - 11 Bonus:Annotated time series
print("\nTask - 11 Bonus:Annotated time series")

url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df=pd.read_csv(url, parse_dates=["Month"], index_col="Month")
df.columns = ["passengers"]

sns.set_theme(style="whitegrid", context="talk")
fig, ax = plt.subplots(figsize=(12,6))
df.plot(y="passengers", ax=ax, color="steelblue", lw=1.5, legend=False)

max_idx = df["passengers"].idxmax()
max_val = df.loc[max_idx,"passengers"]
x_pos = df.index.get_loc(max_idx)
ax.annotate(
    f"Peak: {max_val} passengers ({max_idx.strftime('%b %Y')})",
    xy=(x_pos,max_val),
    xytext=(x_pos-24, max_val-40),
    arrowprops = dict(arrowstyle="->", color="red", lw=1.5),
    fontsize=11,
    color="red",
    ha="center"
)

yearly = df["passengers"].resample("YE").sum()
yoy_growth = yearly.pct_change()*100
best_year = yoy_growth.idxmax()
best_growth = yoy_growth.max()

year_mask = df.index.year == best_year.year
best_month_idx = df[year_mask]["passengers"].idxmax()
best_month_val = df.loc[best_month_idx, "passengers"]
best_x_pos = df.index.get_loc(best_month_idx)

ax.annotate(
    f"Biggest YoY growth: {best_growth:.1f}% in {best_year.year}",
    xy=(best_x_pos, best_month_val),
    xytext=(best_x_pos+12,best_month_val*0.55),
    arrowprops=dict(arrowstyle="->", color="green", lw=1.5),
    fontsize=11,
    color="green",
    ha="left"
)

ax.set_title("Airline Passengers 1949-1960", fontsize=14, fontweight="bold")
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Passengers (thousands)", fontsize=12)

plt.tight_layout()
plt.savefig("airline_annotated.png", dpi=300, bbox_inches="tight")
plt.show()

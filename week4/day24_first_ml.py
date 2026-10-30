import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Task 1 - Simple regression
print("\nTask 1 - Simple regression")
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
tips = pd.read_csv(url)
X = tips[["total_bill"]]
y = tips["tip"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print(f"Intercept (B0): {model.intercept_:.4f}")
print(f"Coefficient (B1): {model.coef_[0]:.4f}")
# prediction for $50 bill is $6.27
print(model.predict([[50]]))

# Task2 - Evaluate
print("\nTask 2 - Evaluate")
print(tips.shape)
print(tips["total_bill"].mean())
print(tips["tip"].mean())
print(X_train.shape, X_test.shape)

mae = mean_absolute_error(y_test, y_pred) # on average, prediction are offset by $0.62
rmse = np.sqrt(mean_squared_error(y_test, y_pred)) # on average, prediction are offset by 0.75
r2_1 = r2_score(y_test, y_pred)# how much variance the model explain. if R2=1 perfect prediction, if R2=0 prediction is always the mean, if R2<0, prediction is worst than predicting the mean

print(f"\nMAE = {mae:.2f}\nRSME= {rmse:.2f}\nR2= {r2_1:.4f}")
# R2 = 0.5449 means the model explains 54.49% of tip variance. the remaining 45% is due to factors
# not captured by total_bill (service quality, day, size). RSME of $0.75 means typical predictions are off bo +/- $0.75

# Task3 - Multi-feature regression
print("Task 3 - Multi-feature regression")

X = tips[["total_bill", "size"]]
y = tips["tip"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
mae2 = mean_absolute_error(y_test, y_pred)
rsme2 = np.sqrt(mean_squared_error(y_test, y_pred))
r2_2 = r2_score(y_test, y_pred)

print(f"\nMAE= {mae2:.2f}\nRSME= {rsme2:.2f}\nR2= {r2_2:.4f}") # Adding size did not improve test performance, slighlty overfitting
# Reason: size and total_bill are correlated (r = 0.6), and the small extra signal is outweighed by noise on this small test set

# Task 4 - Add a categorical feature
print("Task 4 - Add a categorical feature")
X = tips[["total_bill", "size"]].copy()
X["is_female"] = (tips["sex"] == "Female").astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
mae3 = mean_absolute_error(y_test, y_pred)
rsme3 = np.sqrt(mean_squared_error(y_test, y_pred))
r2_3 = r2_score(y_test, y_pred)

print(f"\nMAE= {mae3:.2f}\nRSEM= {rsme3:.2f}\nR2= {r2_3:.4f}") # There is no improvement in the model

# Task 5 - Try another target
print("Task 5 - Try another target")
X = tips[["tip", "size"]]
y = tips["total_bill"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mae4 = mean_absolute_error(y_test, y_pred)
rsme4 = np.sqrt(mean_squared_error(y_test, y_pred))
r2_4 = r2_score(y_test, y_pred)

print(f"\nMAE= {mae4:.2f}\nRSME= {rsme4:.2f}\nR2= {r2_4:.4f}") # This is not a good model, R2 is close to 0

# Task 6 - Visualize
print("Task 6 - Visualize")
X = tips[["total_bill", "size"]]
y = tips["tip"]
X_train, X_test, y_train, y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

fig, ax = plt.subplots(figsize=(10,6))

ax.scatter(y_test,y_pred, label="Predictions", alpha=0.5, color="steelblue")
#ax.scatter(X_test["tip"], y_pred, label="Predicted", color="red", marker="*", alpha=0.5)
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
ax.plot([min_val, max_val],[min_val, max_val], color="red", lw=2, linestyle="--", label="Perfect prediction")
ax.set_title("Actual vs Predicted Tip (Test Set)", fontsize=14)
ax.set_xlabel("Actutal Tip ($)")
ax.set_ylabel("Predicted Tip ($)")
r2 = r2_score(y_test, y_pred)
ax.annotate(
    f"R2 = {r2:.3f}\nMAE = ${mean_absolute_error(y_test,y_pred):.2f}",
    xy = (0.05,0.85),
    xycoords="axes fraction",
    fontsize=12,
    bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="gray")
)
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig("model_performance.png", dpi=300, bbox_inches="tight")
plt.show()

# Task 7 - Compare train vs test
print("Task 7 - Compare train vs test")
y_train_pred = model.predict(X_train)
mae_train = mean_absolute_error(y_train,y_train_pred)
mae_test = mean_absolute_error(y_test,y_pred)
rsme_train = np.sqrt(mean_squared_error(y_train,y_train_pred))
rsme_test = np.sqrt(mean_squared_error(y_test,y_pred))
r2_train = r2_score(y_train,y_train_pred)
r2_test = r2_score(y_test,y_pred)
print(f"\nMAE on training set: {mae_train:.2f}\nMAE on test set: {mae_test:.2f}")
print(f"RSME on training set: {rsme_train:.2f}\nRSME on test set: {rsme_test:.2f}")
print(f"R2 on training set: {r2_train:.2f}\nR2 on test set: {r2_test:.2f}")
# are are quite close, train data result are little bit higher because of the sample size compare to test size data

# Task 8 - Bonus: Real dataset (Boston-like)
print("Task 8 - Bonus: Real dataset (Boston-like)")
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing(as_frame=True)
df = housing.frame
print(df.head())
print(df.describe())

X = df[["MedInc"]]
y = df["MedHouseVal"]   
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rsme = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"\nMAE = {mae:.2f}\nRSME = {rsme:.2f}\nR2 = {r2:.4f}")
# with R2<0, income is not a good predictor

# Task 9 - Bonus: Multi-feature housing
print("Task 9 - Bonus: Multi-feature housing")
X = df[["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup",
"Latitude", "Longitude"]]

y = df[["MedHouseVal"]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rsme = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"\nMAE = {mae:.2f}\nRSME = {rsme:.2f}\nR2 = {r2:.4f}")
# R2 is now 0.3377 with a better model compare to the first on variable model. eventhough 33% of variance this new model is explaining, there is still other parameters that can improve the model
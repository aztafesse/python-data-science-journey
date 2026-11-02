import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Task 1 - Residual analysis
print("\nTask 1 - Residual analysis")
tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

X = tips[["total_bill"]]
y = tips["tip"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)
residuals = y_test - y_pred

fig, axes = plt.subplots(1,3,figsize=(16,5))
axes[0].scatter(y_pred, residuals, alpha=0.6)
axes[0].set_title("Residual vs Predicted", fontsize=14)
axes[0].set_xlabel("Tips ($)")
axes[0].set_ylabel("Residuals")

axes[1].hist(residuals, bins=20, edgecolor="black")
axes[1].set_title("Residuals Distribution")
axes[1].set_xlabel("Residuals")

from scipy import stats
stats.probplot(residuals, plot=axes[2])
axes[2].set_title("QQ_Plot")
plt.tight_layout()
plt.show()
# Residuals are roughly center at 0 and mostly random, but the right tail of the hist plot and the upper deviation
# on the QQ plot show a positive skew. the model underestimates some large tips. Mild heteroscedasticity
# presnt (residual spread grows slightly with predicted tip)

# Task 2 - Multicollinearity check
print("\nTask 2 - Multicollinearity check")
tips_corr = tips[["total_bill", "size", "tip"]]
tips_corr_result = tips_corr.corr()
print(tips_corr_result) # corr("total_bill", "tip") = 0.6757 > 0.6
# Feature - feature correlation: total_bill <-> size = 0.60 -- moderate multicollinearity
# total_bill <-> tip = 0.68 is the target correlation -- that's the predictive signal we want.
# size <-> tip = 0.49 confirms both features carry some tip signal

# Task 3 - Feature scaling
print("\nTask 3 - Feature scaling")
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X = tips[["total_bill", "size"]]
y = tips["tip"]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=42)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_scaled = LinearRegression().fit(X_train_scaled,y_train)
model_unscaled = LinearRegression().fit(X_train, y_train)
print(f"\nIntercept: Unscaled B0 = {model_unscaled.intercept_:.4f}")
print(f"Coefficient: Unscaled B1 = {model_unscaled.coef_[0]:.4f} (total_bill), B2 = {model_unscaled.coef_[1]:.4f} (size)")
print(f"\nIntercept: Scaled B0 = {model_scaled.intercept_:.4f}")
print(f"Coefficient: Scaled B1 = {model_scaled.coef_[0]:.4f} (total_bill), B2 = {model_scaled.coef_[1]:.4f} (size)")

# after scaling, coefficients are in std units which is directly comparable. Unscaled coefficients have inconsistent
# units (dollar vs people), so comparing the magnitude is meaningless. Scalling makes the model
# interpretable across feature


# Task 4 - Ridge regression
print("\nTask 4 - Ridge regression")
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
X = tips [["total_bill", "size"]]
y = tips["tip"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
alphas = [0.001, 0.01, 0.1, 1, 10, 100]
for a in alphas:
    scores = cross_val_score(Ridge(alpha=a), X_train, y_train, cv=5, scoring="r2")
    print(f"\nalpha={a:6.3f}| Mean R2 = {scores.mean():.4f} +/- {scores.std():.4f}")
# Ridge R2 is fairly stable across alphas 0.001 - 1, dropping slightly at alpha = 10-100.
# Regularization doesn't help much here because we only have 2 features. Ridge is best when there are
# many correlated features

# Task 5 - Lasso regression
print("Task 5 - Lasso regression")
from sklearn.linear_model import Lasso
for a in alphas:
    lasso = Lasso(alpha=a).fit(X_train, y_train)
    print(f"alpha={a:6.3f}: coef = {lasso.coef_}")
# at Alpha = 1, the size coefficeint is driven to exactly 0 - Lasso dropped the feature. This is Lasso's
# feature-selection behavior: it favors total_bill (stronger prediction) and eliminates size
# (weaker, partly redundant)


# Task 6 - Pipeline
print("Task 6 - Pipeline")
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

pipe = Pipeline([("scaler", StandardScaler()), ("model", Ridge())])
 
grid = GridSearchCV(
    Pipeline([("scaler", StandardScaler()), ("ridge", Ridge())]),
    {"ridge__alpha": [0.01, 0.1, 1, 10]},
    cv=5,
    scoring="r2"
)
grid.fit(X_train, y_train)
print(f"\nBest Ridge alpha: {grid.best_params_['ridge__alpha']}")
print(f"Best CV R2: {grid.best_score_:.4f}")
# Best Ridge alpha = 0.1, best CV R2 = 0.46 - essentially identical to unregularized Linear
# Regression. With only 2 features, regularization adds little value

# Task 7 - Cross validation comparison
print("Task 7 - Cross validation comparison")

for name, pipe in [
    ("Linear", Pipeline([("m", LinearRegression())])),
    ("Ridge 1", Pipeline([("scaler", StandardScaler()), ("m", Ridge(1.0))])),
    ("Lasso 0.1", Pipeline([("Scaler", StandardScaler()),("m", Lasso(0.1))])),
]:
    scores = cross_val_score(pipe, X, y, cv=5, scoring="r2")
    print(f"{name:10s}: {scores.mean():.4f} +/- {scores.std():.4f}")
# Lasso 0.1 generalize best
# All 3 models perform almost identically R2 = 0.44-0.47. This confirms that on small feature
# sets, regularization offers little benefit.
# Task 8 - California housing
print("Task 8 - California housing")
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import r2_score
housing = fetch_california_housing(as_frame=True)
df = housing.frame

X = df[["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]]
y = df["MedHouseVal"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model_lr = LinearRegression().fit(X_train,y_train)
y_pred_lr = model_lr.predict(X_test)
r2_lr = r2_score(y_test, y_pred_lr)
print(f"Linear Regression: R2 = {r2_lr:.4f}")

grid = GridSearchCV(
    Pipeline([("Scaler", StandardScaler()), ("ridge", Ridge())]),
    {"ridge__alpha":[0.01, 0.1, 1, 10]}, cv=5, scoring="r2"
)
grid.fit(X_train, y_train)
print(f"\nBest Ridge alpha: {grid.best_params_['ridge__alpha']}")
print(f"Best CV R2:     {grid.best_score_:.4f}")

grid = GridSearchCV(
    Pipeline([("Scaler", StandardScaler()), ("lasso", Lasso())]),
    {"lasso__alpha":[0.001, 0.01, 0.1, 1]}, cv=5, scoring="r2"
)
grid.fit(X_train, y_train)
print(f"\nBest Lasso alpha: {grid.best_params_['lasso__alpha']}")
print(f"Best CV R2:     {grid.best_score_:.4f}")
# Ridge 0.01 and Lasso 0.001 both achieve CV R2 = 0.6115, only slightly better than plain 
# Regression. The 8 features aren't highly correlated with each other, so regularization gives small gains

# Task 9 - Bonus: Use Lasso for feature selection
print("Task 9 - Bonus: Use of Lasso for feature selection")
model_lasso = Pipeline([
    ("scaler", StandardScaler()),
    ("model", Lasso(0.1))
])
model_lasso.fit(X_train, y_train)
coefficients = model_lasso.named_steps["model"].coef_
feature_name = model_lasso["scaler"].get_feature_names_out()

coef_summary = pd.Series(coefficients, index=feature_name)
print(coef_summary)
# MedInc feature matter the most following by HouseAge.
# All remaining features are useless
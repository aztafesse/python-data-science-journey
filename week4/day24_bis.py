import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

tips=pd.read_csv(url)

X = tips[["total_bill"]]
y = tips["tip"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression().fit(X_train,y_train)
y_pred = model.predict(X_test)

residuals = y_test - y_pred

fig, axes = plt.subplots(1, 3, figsize=(15,4))

axes[0].scatter(y_pred, residuals, alpha=0.6)
axes[0].axhline(0, color="red", linestyle="--")
axes[0].set_xlabel("Predicted")
axes[0].set_ylabel("Residual")
axes[0].set_title("Residuals vs Predicted")

axes[1].hist(residuals, bins=20, edgecolor="black")
axes[1].set_title("Distribution of Residuals")
axes[1].set_xlabel("Residual")

from scipy import stats
stats.probplot(residuals, dist="norm", plot=axes[2])
axes[2].set_title("QQ Plot")

plt.tight_layout()
plt.show()

num_df = tips.select_dtypes(include="number")
corr = num_df.corr()

fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1, ax=ax)
plt.show()

from statsmodels.stats.outliers_influence import variance_inflation_factor

X_multi = tips[["total_bill", "size"]]
vif = pd.DataFrame()
vif["feature"] = X_multi.columns
vif["VIF"] = [variance_inflation_factor(X_multi.values, i)
              for i in range(X_multi.shape[1])]

print(vif)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

from sklearn.linear_model import Ridge

model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

from sklearn.linear_model import Lasso

model = Lasso(alpha=0.1)
model.fit(X_train, y_train)
print(dict(zip(X_train.columns, model.coef_)))

from sklearn.linear_model import ElasticNet
model = ElasticNet(alpha=1.0, l1_ratio=0.5)

from sklearn.model_selection import cross_val_score, GridSearchCV
alphas = [0.001, 0.01, 0.1, 1, 10, 100]

for a in alphas:
    scores = cross_val_score(Ridge(alpha=a), X_train, y_train, cv=5, scoring="r2")
    print(f"alpha={a:6.3f} CV R2 = {scores.mean():.4f}")

grid = GridSearchCV(Ridge(), {"alpha":alphas}, cv=5, scoring="r2")
grid.fit(X_train, y_train)
print(f"Best alpha: {grid.best_params_}")
print(f"Best CV R2: {grid.best_score_:.4f}")

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", Ridge(alpha=1.0))
])

pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)

scores = cross_val_score(pipe, X, y, cv=5, scoring="r2")
print(f"CV R2: {scores.mean():.4f} +/- {scores.std():.4f}")

from sklearn.model_selection import GridSearchCV

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("ridge", Ridge())
])

params = {"ridge__alpha": [0.01, 0.1, 1, 10, 100]}
grid = GridSearchCV(pipe, params, cv=5, scoring = "r2")
grid.fit(X_train, y_train)
print(f"Best alpha: {grid.best_params_}")
print(f"Best CV R2: {grid.best_score_:.4f}")

from sklearn.model_selection import cross_val_score, KFold

kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(LinearRegression(), X, y, cv=kf, scoring="r2")

print(f"Fold R2s: {scores}")
print(f"Mean R2: {scores.mean():.4f}")
print(f"Std R2: {scores.std():.4f}")
print(kf)


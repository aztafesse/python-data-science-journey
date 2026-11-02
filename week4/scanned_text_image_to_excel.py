import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import Ridge

tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
X = tips[["total_bill", "size"]]
y = tips["tip"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

kf = KFold(n_splits=5, shuffle=True, random_state=42)

alphas = [0.001, 0.01, 0.1, 1, 10, 100]

print("=" * 60)
print("TASK 4 — Ridge Regression (KFold shuffled)")
print("=" * 60)

results = []
for a in alphas:
    scores = cross_val_score(
        Ridge(alpha=a),
        X_train, y_train,
        cv=kf,
        scoring="r2"
    )
    results.append(scores.mean())
    print(f"alpha={a:8.3f} | Fold R²s: {np.round(scores, 4)} | Mean = {scores.mean():.4f} ± {scores.std():.4f}")

best_alpha = alphas[int(np.argmax(results))]
print(f"\n>> Best alpha = {best_alpha}")
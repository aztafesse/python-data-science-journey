import sklearn 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

print(f"sklearn version: {sklearn.__version__}")
print(f"numpy version: {np.__version__}\n")


url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

tips=pd.read_csv(url)

X_tb = tips[["total_bill"]]
X_tb_s = tips[["total_bill", "size"]]
y = tips["tip"]

Xt, Xv, yt, yv = train_test_split(X_tb, y, test_size=0.2, random_state=42)
Xt2, Xv2, yt2, yv2 = train_test_split(X_tb_s, y, test_size=0.2, random_state=42)

m1 = LinearRegression().fit(Xt,yt)
m2 = LinearRegression().fit(Xt2,yt2)

r2_1 = r2_score(yv, m1.predict(Xv))
r2_2 = r2_score(yv2, m2.predict(Xv2))

print(f"Task 2 (total_bill only):       R2 = {r2_1:.4f})")
print(f"Task 3 (total_bill + size):      R2 = {r2_2:.4f}")
print(f"Difference: {(r2_2-r2_1)*100:+.2f} percentage points\n")

cv1 = cross_val_score(LinearRegression(), X_tb, y, cv = 10, scoring = "r2")
cv2 = cross_val_score(LinearRegression(), X_tb_s, y, cv = 10, scoring = "r2")

print(f"CV 10-fold R2 total_bill:     {cv1.mean():.4f} +/- {cv1.std():.4f}")
print(f"CV 10-fold total_bill + size: {cv2.mean():.4f} +/- {cv2.std():.4f}")



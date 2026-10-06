import numpy as np

# Task 1 - BAsic aggregations
a = np.array([12, 7, 3, 15, 9, 22, 5, 18])
print(a.sum())
print(a.mean())
print(a.min())
print(a.max())
print(a.std())
print(a.var())
print(a.argmin())
print(a.argmax())
print(np.percentile(a,[25, 50, 75]))
print(np.cumsum(a,axis = 0))

# Task 2 - Axis practice
m = np.array([[3, 7, 2],
              [8, 1, 9],
              [5, 6, 4]])
computed_sum = m.sum()  # result 45
computed_mean = m.mean() # result 5
computed_min = m.min()   # result 1
computed_max = m.max()  # result 9
print(f"For whole array\n Sum: {computed_sum}\n Mean: {computed_mean}\n Min: {computed_min}\n Max: {computed_max}")

computed_sums_axis0 = m.sum(axis=0)
computed_means_axis0 = m.mean(axis=0)
computed_mins_axis0 = m.min(axis=0)
computed_maxs_axis0 = m.max(axis=0)
print(f"Per column (axis = 0)\n Sums: {computed_sums_axis0}\n Means: {computed_means_axis0}\n Mins: {computed_mins_axis0}\n Maxs: {computed_maxs_axis0}")

computed_sums_axis1 = m.sum(axis=1)
computed_means_axis1 = m.mean(axis=1)
computed_mins_axis1 = m.min(axis=1)
computed_maxs_axis1 = m.max(axis=1)
print(f" Per row (axis = 1)\n Sums: {computed_sums_axis1}\n Means: {computed_means_axis1}\n Mins: {computed_mins_axis1}\n Max: {computed_maxs_axis1}")

# Task 3 - argmin/argmax
data = np.array([[10, 20, 30],
                 [40, 5, 60],
                 [7, 80, 90]])
print(data.argmax())
print(data.argmax(axis=0))
print(data.argmax(axis=1))

# Task 4 - Cumulative
a = np.array([2, 4, 6, 8, 10])
print(a.cumsum())
print(a.cumprod())

m = np.array([[1, 2], [3, 4], [5, 6]])
print(m.cumsum(axis=0))
print(m.cumsum(axis=1))

# Task 5 - keepdims
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(f"Means: {m.mean(axis=0)} and Shape: {m.mean(axis=0).shape}")
print(f"Means: {m.mean(axis=0, keepdims = True)} and Shape: {m.mean(axis=0, keepdims = True).shape}")
print((m-m.mean(axis=0,keepdims = True)).mean(axis=0))

# Task 6 - Missing data
a = np.array([5, np.nan, 8, 12, np.nan, 20])
print(f"a: {a}, and dtype: {a.dtype}")
print(f" Sum: {a.sum()}, and Mean: {a.mean()}")
print(f" Sum: {np.nansum(a)}, mean: {np.nanmean(a)}, max = {np.nanmax(a)}")
print(np.isnan(a).sum())
a[np.isnan(a)] = 0
print(a)

# Task 7 - Real-world data summary
scores = np.array([[85, 90, 78],
                   [70, 65, 80],
                   [95, 88, 92],
                   [60, 75, 70],
                   [88, 82, 85]])

print(f"Each student's average: {scores.mean(axis=1)}")
print(f"Each students's highest score: {scores.max(axis=1)}")
print(f"Class average per subject: {scores.mean(axis=0)}")
print(f"Highest score per subject: {scores.max(axis=0)}")
print(f"Overall class average: {scores.mean()}")
print(scores.mean(axis=1).argmax())

# Task 8 - Bonus: Percentile analysis
scores = np.array([56, 78, 90, 45, 88, 92, 67, 71, 83, 95, 62, 77])
print(np.percentile(scores, [10, 25, 50, 75, 90]))
print(f"Interquartile range IQR(Q3-Q1): {np.percentile(scores,75)-np.percentile(scores,25)}")
print(f" Number of scores above 75th percentile: {(scores>np.percentile(scores,75)).sum()}")

import numpy as np

# Task 1 - Scalar broadcasting
a = np.array([5, 10, 15, 20])
print(a +100)
print(a*3)
print(a/5)
print(a**2)

# TAsk 2 - Same - shape operations
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a+b)
print(a*b)
print(a/b)
print(a-b)

# Task 3 - 1D + 2D broadcasting
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
row_add = np.array([10, 20, 30])
print(m+row_add)

# Task 4 - Column broadcasting
m = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
col_add = np.array([100, 200, 300])
print(m+col_add)
print(m+col_add.reshape(-1,1))
print(m + col_add[:,np.newaxis])

# Task 5 - Centering
data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])
col_means = data.mean(axis = 0)
print(col_means)
print(data - col_means)
print((data-col_means).mean(axis=0))

# Task 6 - Standardization
data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])
col_means = data.mean(axis=0)
col_stds = data.std(axis=0)
standardize = (data-col_means)/col_stds
print(standardize)
print(standardize.mean(axis=0))
print(standardize.std(axis=0))

# Task 7 - Row-wise operation
print(data)
row_means = data.mean(axis=1)
row_means=row_means.reshape(-1,1)
print((data-row_means).sum(axis = 1))

# Task 8 - Real-world: normilize image-like data
pixels = np.array([[0, 50, 100, 150, 200],
                   [10, 60, 110, 160, 210],
                   [20, 70, 120, 170, 220],
                   [30, 80, 130, 180, 230]])
normalize = pixels/255
pixel_means = normalize.mean(axis=0)
print(normalize-pixel_means)

# TAsk 9 - Bonus: Batch processing
batch = np.array([[1.0, 2.0, 3.0, 4.0],
                  [5.0, 6.0, 7.0, 8.0],
                  [9.0, 10.0, 11.0, 12.0]])
bias_vector = np.array([0.1, 0.2, 0.3, 0.4])
print(batch + bias_vector)
weight_vector = np.array([2.0, 1.5, 1.0, 0.5])
print((batch+bias_vector)*weight_vector)
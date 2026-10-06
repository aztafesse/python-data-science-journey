import numpy as np

# Task 1 - 1D slicing
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[2:6])
print(a[7:])
print(a[1::2])
print(a[::-1])

# Task 2 - View vs copies
a = np.array([1, 2, 3, 4, 5])
b = a[1:4]
b[0] = 100
print(a)
print(b)

a = np.array([1, 2, 3, 4, 5])
b = a[1:4].copy()
b[0] = 100
print(a)
print(b)

# Task 3 - 2D indexing
m = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print(m[1,0])
print(m[2])
print(m[:,1])
print(m[2:4,2:4])
print(m[[0,3]][:,[0,2]])

# Task 4 - Fancy indexing
a = np.array([100, 200, 300, 400, 500])
print(a[[0,2,4]])
print(a[[4,0,3]])
indice = np.array([1, 3])
print(a[indice])

# Task 5 - Boolean filtering
data = np.array([12, 5, 8, 20, 3, 15, 7, 25, 18, 2])
print(data[data>10])
print(data[(data>=5) & (data<=20)])
print(data[data %2 ==1])
print((data < 10).sum())
data[data>15] = 0
print(data)

# Task 6 - np.where()
a = np.array([3, 8, 1, 6, 9, 2, 7])
idx = np.where(a>5)
print(idx)
b = np.where(a > 5,"high", "low")
print(b)
print(a[np.where(a>5)])

# Task 7 - Real-word simulation
scores = np.array([[85, 90, 78],
                   [70, 65, 80],
                   [95, 88, 92],
                   [60, 75, 70],
                   [88, 82, 85]])

print(scores[:,0])
print(scores[2,:])
print(scores[scores[:,0] > 80])
print(scores[:,1].mean())
print(scores[(scores[:,0] > 80) & (scores[:,1] > 80)])

# Task 8 - Bonus: Top N
a = np.array([45, 12, 89, 33, 67, 21, 90, 8, 55])
print(a[np.argsort(a)[-3:]])
print(a[np.argsort(a)[:3]])
print(np.argsort(a)[-3:])

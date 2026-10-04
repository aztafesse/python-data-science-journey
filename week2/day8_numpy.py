import numpy as np

# Task 1 - Basic array creation
a = np.array([5, 10, 15, 20, 25])
print(type(a))
print(a.dtype)
print(a.shape)
b = np.zeros(10)
c = np.full(7,5)
print(c)
d = np.arange(1,20,3)
print(d)

# Task 2 - Vectorized math
a = np.array([2, 4, 6, 8, 10])
print(a+5)
print(a*2)
print(a**2)
print(a/2)
print(a[a>5])
print(a.mean())
print(a.max())
print(a.min())
print(a.sum())

# Task 3 - List vs NumPy speed
import time
lst = list(range(1_000_000))
start_time = time.time()
result = [i*3 for i in lst]
laps_list = time.time()-start_time
print(f"List : {laps_list:.5f}s")

arr = np.arange(1_000_000)
start_time = time.time()
result = arr*3
laps_numpy = time.time()-start_time
print(f"NumPy : {laps_numpy:.5f}s")

print(f" Numpy is {round(laps_list/laps_numpy)} times faster than list")

# Task 4 - 2D array basics
m = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

print(m.shape)
print(m.ndim)
print(m.size)
print(m[0,1])
print(m[1,:])
print(m[:,2])
print(m.sum())
print(m.mean())
print(m.max())


# Task 5 - Boolean filtering
data = np.array([12, 5, 8, 20, 3, 15, 7, 25, 18, 2])
print(data[data>10])
print(data[data % 2 == 0])
print(data[(data>= 5) & (data<=20)])
# Method 1
print(data[data > 10].size)
# Method 2
mask = data > 10
print(mask.sum())

# Task 6 - Reshape

data = np.arange(24)
data1 = data.reshape(4,6)
data2 = data.reshape(6,4)
data3 = data.reshape(2,-1)
print(data1)
print(data2)
print(data3)

data4 = data1.flatten()
print(data4)

# Task 7 - Bonus: Column means
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(f"mean of each column: {matrix.mean(axis = 0)}")
print(f"mean of each row : {matrix.mean(axis = 1)}")







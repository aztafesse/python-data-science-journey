import numpy as np
print(np.__version__)

a = np.array([1,2,3,4,5])
print(a)
print(type(a))
print(a.dtype)

# From nested lists
matrix = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(matrix)

print(matrix.shape)
print(matrix.ndim)
print(matrix.size)

print(np.zeros(5))
print(np.ones(3))
print(np.full(4,7))
print(np.arange(0,10,2))
print(np.linspace(0,1,5))
print(np.eye(3))
print(np.random.rand(3))
print(np.random.randint(1,10,5))

# Data types 
a = np.array([1,2,3])
print(a.dtype)

b = np.array([1.0, 2.5, 3.7])
print(b.dtype)

c = np.array([1, 2, 3], dtype=float)
print(c)
print(c.dtype)

d = np.array([True, False, True])
print(d.dtype)

import time

#python list
lst = list(range(1_000_000))
start = time.time()
result = [x * 2 for x in lst]
print(f"List: {time.time() - start:.4f}s")

#NumPy
arr = np.arange(1_000_000)
start = time.time()
result = arr*2
print(f"NumPy: {time.time() - start:.4f}s")

# Vectorize operation

lst = [1, 2, 3, 4]
result = [x+10 for x in lst]

print(result)

arr = np.array([1, 2, 3, 4])
result = arr + 10

m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

a = np.arange(12)
c = a.reshape(2,-1)
print(c)

# Task 1 - Basic array creation
n = np.array([5, 10, 15, 20, 25])
print(type(n))
print(n.dtype)


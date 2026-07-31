#1. Why NumPy?
#Faster than Python lists (implemented in C).
#Supports multi-dimensional arrays.
#Provides mathematical functions (linear algebra, statistics, random numbers).
#Forms the foundation for other libraries like Pandas, SciPy, TensorFlow.

#🔹 2. Creating Arrays


import  numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4])
print(arr1)   # Output: [1 2 3 4]

# 2D array (matrix)
arr2 = np.array([[1, 2], [3, 4]])
print(arr2)
# Output:
# [[1 2]
#  [3 4]]

#🔹 3. Array Operations

arr = np.array([10, 20, 30, 40])

print(arr + 5)     # [15 25 35 45]
print(arr * 2)     # [20 40 60 80]
print(np.mean(arr)) # Average → 25.0
print(np.sqrt(arr)) # Square roots → [3.16 4.47 5.47 6.32]

#🔹 4. Useful Functions

#Function	             Purpose	Example
#np.zeros((2,3))	2x3 matrix of zeros	[[0. 0. 0.],[0. 0. 0.]]
#np.ones((2,2))	2x2 matrix of ones	[[1. 1.],[1. 1.]]
#np.arange(1,10,2)	Range with step	[1 3 5 7 9]
#np.linspace(0,1,5)	Evenly spaced values	[0. 0.25 0.5 0.75 1.]
#np.random.rand(3)	Random numbers	[0.12 0.45 0.89]


#🔹 5. Indexing & Slicing

arr = np.array([5, 10, 15, 20, 25])
print(arr[0])     # 5
print(arr[-1])    # 25
print(arr[1:4])   # [10 15 20]

#🎯 Quick Summary
#NumPy = Fast numerical computing with arrays.
#Arrays are more efficient than lists.
#Provides math, stats, random, and matrix operations.
#Essential for data science, ML, and AI.
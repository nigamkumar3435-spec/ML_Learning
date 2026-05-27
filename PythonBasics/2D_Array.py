#create 2D array
import numpy as np
arr= np.array([[1,2,3],[4,5,6]])
print("Matrix(2D)")
print(arr)

two_d = np.array([[2, 4], [6, 8]])
print("2D:\n", two_d)
#Output: 2D:
 #          [[2 4]
 #           [6 8]]

#Multiplication of two 2x2 Matrix
x=np.array([[2,4],[3,5]])
y=np.array([[2,4],[4,5]])
z=x@y # '@'multiplies the matrix by row and column
print(z)

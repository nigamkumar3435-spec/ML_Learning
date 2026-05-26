import numpy as np

#vector operations (Tensor) space of both the matrix
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[2,2,2],[2,2,2]])
print(a)
print()
print(b)

#arithmetic operations
print(a+b)
print()
print(a-b)
print()
print(a*b)
print()
print(a/b)
print()
print(a**b)
print()
print(a//b)

#max/min/sum/prod
#0-> col and 1-> row
b=np.arange(12).reshape(3,4)
print(b)
print(b.sum())
print(b.sum(axis=0))#column wise
print(b.sum(axis=1))#row wise
print(b.max())
print(b.min())
print(b.max(axis=0))
print(b.min(axis=0))
print(b.prod())

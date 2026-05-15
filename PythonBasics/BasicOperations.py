import numpy as np
import sys

a=range(1000)
print(sys.getsizeof(a))

arr=np.arange(1000)
arr=np.arange(10)
print(arr.itemsize)
print(arr.size)
print(arr)
print(type(arr))

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

#comparing size of array and list
import sys
import numpy as np
l=range(1000)
print("Size of list: ",sys.getsizeof(l)*len(l))
array=np.arange(1000)
print("Size of Numpy array: ",array.size*array.itemsize)

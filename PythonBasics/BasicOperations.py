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

# list operatiion
# append is used to add in the list
a=[i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]
c=[]
import time
start=time.time()
for i in range(len(a)):
  c.append(a[i]+b[i])
print(time.time()-start)

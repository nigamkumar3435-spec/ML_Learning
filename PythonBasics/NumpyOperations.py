#Numpy Operation

import numpy as np
a=np.arange(10000000)
b=np.arange(10000000,20000000)
start=time.time()
c=a+b
print(time.time()-start)

import numpy as np
a=np.array([1,2,4,5])
print(a)
print(type (a))
print(a.ndim)
print(a[1])
#Output: [1 2 4 5]
#        <class 'numpy.ndarray'>
#        1
#        2

a1=np.array([[1,5],[3,4]])
print(a1)
print(type(a1))
print(a1.ndim)
print(a1[0][1])  #this and
print(a1[0,1])   #this wil give the same output
#Output: [[1 5]
 #        [3 4]]
#        <class 'numpy.ndarray'>
#        2
#        5
#        5

#Addition

arr=np.array([1,5,3,4,6])
print(arr[4])
print(arr[3]+arr[4])
#Output: 6
#        10

#3d array treats 2d array as an element.
c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)
print(type(c))
print(c.ndim)
print(c[0][0][0])
print(c[1,1,0])#first 1 is from 3d array, second 1 is from second 2d array, third 0 is from fourth 1d array
print(c[0,1,0])
print(c[0,0,1])

np.array([1,2,3],dtype=complex)

#np.arange creates 1d array
a=np.arange(1,11,2)#(start,stop,step)
print(a)
#a=np.arange(1,11,2) generates 1d matrix

#with reshape
print(np.arange(16).reshape(4,4))

print(np.arange(16,dtype=float).reshape(4,4))
print(np.arange(16).reshape(2,2,4))

#ones - It helps in initialing the matrix
a=np.ones((3,4))
a

#zeros
b=np.zeros((3,4),dtype=int)
print(b)
b

#random
a=np.random.random((3,4))
print(a)

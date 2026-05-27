#create 1D array
import numpy as np
arr=np.array([1,2,3,4])
print("1D Array:",arr)
type(arr)

# Creating 1D array
one_d = np.array([5, 10, 15, 20])
print("1D:", one_d)
#Output: 1D: [ 5 10 15 20]

#create using list
list=[45,3,65,7]
a=np.array(list,dtype=float)
print(a)
a=np.array(list,dtype="U32")
print(a)

#create an array of ones
ones_arr=np.ones((2,4)) #2*4 array of matrix
print("Ones Array:\n",ones_arr)

#create an array with 5 values evenly spaced between 0 and 1
linspace_arr=np.linspace(0,1,5) #5 points between 0 and 1
print(linspace_arr)

#create an array with 5 values evenly spaced between 0 and 1
linspace_arr=np.linspace(0,1,3) #3 points between 0 and 1
print(linspace_arr)


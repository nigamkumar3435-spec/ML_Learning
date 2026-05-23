import numpy as np

a=np.arange(1,11,2)
print(a)   #Output: [1 3 5 7 9]


# random number generation array
a=np.random.random((3,4))
print(a)   
print(a[2][2])

a=np.random.randint(1,100,24)
print(a)  #Output: [27 65 69 54 70 35 82 14 79 60 17 65 31 13  6 51 20 36 37 35 15 57 48 44]

#linspace  
np.linspace(-10,10,6)  # it generates linearly separated points.
#Output:  array([-10.,  -6.,  -2.,   2.,   6.,  10.])

# identity matrix

np.identity(3, dtype=int)
np.identity(2, dtype=int)

arr=np.empty(3) # memory allocate  # dtype = int
print(arr)

for i in range(3):
  arr[i]=int(input("Enter the value: "))
print(arr)

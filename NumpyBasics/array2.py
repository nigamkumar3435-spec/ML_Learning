a1=np.arange(10)
a2=np.arange(12,dtype=np.float64).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)
print(a1)
print()
print(a2)
print()
print(a3)

#ndim --what type of array it is
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

#shape --what size of array is (in tuple)
print(a1.shape)
print(a2.shape)
print(a3.shape)

#size --how much elements are there in array
print(a1.size)
print(a2.size)
print(a3.size)


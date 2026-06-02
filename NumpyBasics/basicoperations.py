import numpy as np

b=np.arange(12).reshape(3,4)
print(b)
print(b.sum(axis=0))
print(b.sum(axis=1))

a1=np.arange(6).reshape(2,3)
a2=np.arange(6,12).reshape(3,2)
print(a1)
print(a2)
print(np.dot(a1,a2))

#trigonomatric functions
print(np.sin(a1)) # radians
print(np.cos(a1))

#log Base e and exponents
print(a1)
print(np.log(a1))
print("-"*50)
print(np.exp(a1))

#round /floor/ceil
a=np.random.random((2,3))
a=a*100
print(a)
print(np.round(a))
print(np.floor(a))  #privious integer pr round off
print(np.ceil(a))  #increase by one integer

print(np.floor(85.0940))
print(np.ceil(85.0940))

arr=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(arr[1:,1:3])
print(arr[::2,::3])
print(arr[0:1,1:4])
print(arr[1][0])
print(arr[1,0])

#Transpose
print(a2)
print(np.transpose(a2))
print(a2.T)

a3=np.arange(8).reshape(2,2,2)
print(a3)
i=a3.ravel() #multi dim array converting into 1d array
print(i)
i[0]=100
print(a3) # It changes in original value
print(i)

a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)
print(np.hstack((a4,a5))) #Horizontal Stacking
print("-------------------------")
print(np.vstack((a4,a5))) #Vertical Stacking
print("-------------------------")
#split function
print(np.hsplit(a4,2))
print("-------------------------")
print(np.vsplit(a4,3))

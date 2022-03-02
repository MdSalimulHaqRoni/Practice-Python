from numpy import *
array1 = array([
    [1, 2, 3, 4, 5, 11],
    [6, 7, 8, 9, 10, 12]
])
print(array1) #.size,ndim,shape
array2 = array1.flatten() #dimension conversion
print("1D =",array2)
array3 = array2.reshape(3, 4)
print(array3)
array4 = array2.reshape(2, 2, 3)
print(array4)
print(array4.ndim)
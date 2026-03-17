#Understanding Type, Dimensions, Shape, Size, Data-type, Item-size, N-bytes
import numpy as np
print ("\n1D Array:\n")
a = np.array ([1, 2, 3])
print ("Array -> a: \n", a)
print ("\tType of Array a -> type (a):", type (a))

b = np.array ([
    [1, 2, 3],
    [4, 5, 6],
])
print ("\nArray -> b: \n", b)
print ("\tType of Array b -> type (a)", type (a))

c = np.array ([
    [[1, 2, 3]], [[4, 5, 6]],
    [[7, 8, 9]], [[10, 11, 12]]
])
print ("\nArray -> c: \n", c)
print ("\tType of Array b ->type (c)", type (c))

#ndim
print ("\n\na.ndim :", a.ndim)
print ("b.ndim :", b.ndim)
print ("c.ndim :", c.ndim)

#shape
print ("\n\na.shape :", a.shape)
print ("b.shape :", b.shape)
print ("c.shape :", c.shape)

#size
print ("\n\na.size :", a.size)
print ("b.size :", b.size)
print ("c.size :", c.size)

#datatype
print ("\n\na.dtype:",b.dtype)
print ("b.dtype:",b.dtype)
print ("c.dtype:",c.dtype)

#itemsize
print ("\n\na.itemsize:", a.itemsize)
print ("b.itemsize:", b.itemsize)
print ("c.itemsize:", c.itemsize)

#nbytes
print ("\n\na.nbytes:",a.nbytes)
print ("b.nbytes:",b.nbytes)
print ("c.nbytes:",c.nbytes)

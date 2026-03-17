#indexing and slicing in 2D array

#indexing
b = np.array ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print ("b[1, 2]:", b[1, 2])
print ("b[2, 2]:", b[2, 2])
print ("b[1, 1]:", b[1, 1])
print ("b[-1, -1]:", b[-1, -1])

#slicing
print ("\n\nb[0:2, 1:3]:\n", b[0:2, 1:3])
print ("b[1:2, 1:2]:\n", b[1:2, 1:2])

#indexing + slicing
print ("\n\nb[1, 0:2]:", b[1, 0:2])

import numpy as np
a = np.array ([10, 20, 30, 40, 50])

# Indexing 
print ("Indexing:\na[1]:", a[1])
print ("a[-1]:", a[-1])

'''
Slicing: array [start : stop : step]
'''
print ("\nSlicing:\na[1:3]:", a[1:3])
print ("a[-3:-1]:", a[-3:-1])
print ("a[1:2]:", a[1:2])
print ("a[0:4:-2]:", a[0:4:-2])

print ("a[::-1]", a[::-1])

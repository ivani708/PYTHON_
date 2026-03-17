import numpy as np

# Fancy Indexing
a = np.array ([10, 20, 30, 40, 50])
indices = [0, 2, 4]
b = a [indices]
print ("b:", b)

# Boolean Masking
mask = (a > 20) & (a < 50)
print (mask)
c = a[mask]
print ("Masked Value of c:", c)

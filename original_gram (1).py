import numpy as np
import random
from numpy import linalg as LA

# Making the given matrix
A = np.zeros([11,8])
value = 2.0
counter = 0
for i in range(0,11):
    A[i][0] = 1
    for j in range(1,8):
        A[i][j] = value**j
    value += 0.2
    counter += 1



print(A[:, 2])
y = A[:, 2]
y1 = y - (r * q)
q = y1/LA.norm(y1)
r = np.dot(y, q)
print(r)



n = len(A[0])
r = np.zeros([n,n])
for i in range(n):
    y1 = A[:, i]
    r[i][i] = LA.norm(y1)
    for j in range(i+1,8):
        y = A[:, j]
        q = y1/LA.norm(y1)
        r[i][j] = np.dot(y, q)
        y1 = y - (r[i][j] * q)
#    r[i][i] = LA.norm(y)
    #q = y/r[i][i]
#    print(q)
print(r)





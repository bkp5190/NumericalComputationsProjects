import numpy as np
import random
from numpy import linalg as LA

#Helper function to multiply matrices
def mult_matrices(A, B):
    result = np.zeros([A.shape[0], B.shape[0]])
    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
#Making the given matrix
A = np.zeros([11,8])
value = 2.0
for i in range(0,11):
    A[i][0] = 1
    for j in range(1,8):
        A[i][j] = value**j
    value += 0.2

#Original Gram-Schmidt
m, n = A.shape
q = np.zeros([m,n])
r = np.zeros([n,n])
for j in range(0,len(A[0])):
    y = A[:,j]
    for i in range(0, j):
        r[i, j] = np.dot(A[:,j],q[:,i])
        y -= r[i, j] * q[:,i]
    r[j, j] = LA.norm(y)
    q[:,j] = y / r[j, j]
print(r)
print(q)
print(mult_matrices(q, r))
#Modified Gram-Schmidt
q = np.zeros([11,8])
r = np.zeros([8,8])
for j in range(0,len(A[0])):
    y = A[:,j]
    for i in range(0, j):
        r[i, j] = np.dot(y,q[:,i])
        y -= r[i, j] * q[:,i]
    r[j, j] = LA.norm(y)
    q[:,j] = y / r[j, j]
print(r)
print(q)







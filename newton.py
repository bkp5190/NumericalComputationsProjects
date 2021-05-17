import math
import numpy as np

def inter_pol(x, y):
    n = len(y)
    d = np.zeros([n, n])
    d[:,0] = y

    j = 2
    i = 1

    for j in range(1,n):
        for i in range(n-j):
            d[i][j] = (d[i+1][j-1] - d[i][j-1]) / (x[i+j] - x[i])

    c = d[0,:]
    return c
x = np.array([5, 10, 15])
y = np.array([math.exp(4), math.exp(9), math.exp(14)])
print(inter_pol(x, y))
#
#def evalp_Newton(t, c, x):
#    n = len(c)
#    p = c(n)
#    for i=(n-1) 
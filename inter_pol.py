import math
import numpy as np
import matplotlib.pyplot as plt

p = []
def inter_pol(x, y):
    n = len(y)
    d = np.zeros([n, n])
    d[:,0] = y

    for j in range(1,n):
        for i in range(n-j):
            d[i][j] = (d[i+1][j-1] - d[i][j-1]) / (x[i+j] - x[i])

    c = d[0,:]
    return c

def evalp_Newton(t, c, x):
    n = len(c)
    p = c[n-1]
    for k in range(n, 1, -1):
        p = p*(t-x[i]) + c[i]
    return p

x = np.array([5, 10, 15])
y = np.array([math.exp(4), math.exp(9), math.exp(14)])
c = inter_pol(x, y)

x_new = []
y_new = []

for i in np.arange(-1, 10.001, .001):
    x_new.append(i)
    y_new.append(evalp_Newton(x_new, c, x))

plt.plot(x_new, evalp_Newton(x_new, c, x))
plt.plot(x, y)
plt.show()
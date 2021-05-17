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
    for k in range(n-1, 0, -1):
        p = p*(t-x[k-1]) + c[k-1]
    return p

x5 = np.linspace(-1,10,5)
x10 = np.linspace(-1,10,10)
x15 = np.linspace(-1,10,15)
x_new = np.linspace(-1,10,1000)

y5 = np.exp(x5-1)
y10 = np.exp(x10-1)
y15 = np.exp(x15-1)
y_new = np.exp(x_new-1)

c5 = inter_pol(x5, y5)
c10 = inter_pol(x10, y10)
c15 = inter_pol(x15, y15)

y5_new = evalp_Newton(x_new, c5, x5)
y10_new = evalp_Newton(x_new, c10, x10)
y15_new = evalp_Newton(x_new, c15, x15)

y5_err = np.abs(y_new - y5_new)
y10_err = np.abs(y_new - y10_new)
y15_err = np.abs(y_new - y15_new)

print('Max error for n=5:',max(y5_err))
print('Max error for n=10:',max(y10_err))
print('Max error for n=15:',max(y15_err))

plt.plot(x_new, y_new)
plt.plot(x_new, y5_new)
plt.plot(x_new, y10_new,'--')
plt.plot(x_new, y15_new,':')
plt.show()
import math
import numpy as np

def evalp_Newton(t, c, x):
    n = len(t) - 1
    p = c[n]
    for k in range(1,n+1):
        p = c[n-k] + (x - t[n-k])*p
    return p
c = inter_pol(x,y)
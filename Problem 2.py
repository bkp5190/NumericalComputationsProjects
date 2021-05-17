import numpy as np

def D(x,h):
    return((f(x+h)-f(x-h))/(2*h))

def Extrapolation(n,D1,D2):
    return(((4**n)*D2-D1)/((4**n)-1))

def f(x):
    return(np.sin(x**2+x/3))


lst = []
value = 1/8

for i in range(0, 4):
	lst.append(value)
	value = value/2
h = np.array(lst)
n = h.shape[0]

x = 0

inter = np.zeros([n,n])

inter[:,0] = D(x,h)

def problem_2():
	for i in range(1,n):
		for j in range(len(h)-i):
			inter[j,i] = Extrapolation(2**i,inter[j,i-1],inter[j+1,i-1])
	return inter
	
print(problem_2())


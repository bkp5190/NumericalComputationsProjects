import math
import matplotlib.pyplot as plt
from scipy.stats import linregress

x0 = 1
x1 = 2
en = []
en1 = []
counter = 0

# code from class
def f(x):
	return (math.exp(x) + x -7)

def secant(x0, x1):
	return (x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0)))

while counter < 100 and x0 != x1:
	x2 = secant(x0, x1)
	x0 = x1
	x1 = x2
	# calculated r value at 1.67
	# |en+1|
	en.append(abs(1.672821 - x1))
	# counter 
	counter += 1

	# |en|
for i in en[1:]:
	en1.append(i)

# remove one element to allow the correct graph
en.pop()

# create log-log graph
plt.xscale("log")
plt.yscale("log")

# plot |en| by |en+1|
plt.plot(en1, en)

# use linear regression function to find the slope with other values
print(linregress(en1, en))

# show the graph
plt.show()
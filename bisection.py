import numpy as np

def f(x):

	return np.log(x) + x**2 - 3

def bisection(f, a, b, TOL):

	while ((b - a)/2) > TOL:

		c = (a + b)/2

		if f(c) == 0:
			return c
		else:

			if round(f(c), 8) == 0:
				return round(c, 8)

			if f(a) * f(c) < 0:
				b = c
			else:
				a = c
TOL = 1/2 * (10**-8)
print(bisection(f, 1, 10, TOL))
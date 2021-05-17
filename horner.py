def horner(expr, n, x):
# skeleton code from class lectures without utilizing "d"
	p = expr[0]
	d = 0
	for i in range(1, n):
		p = p * x + expr[i]
	return p

# list to hold all the coefficients (50)
expr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# desired x value to compute
x = 1.00001

n = len(expr)

print("Expression value at 1.00001: ", horner(expr, n, x))

# error calculation
y = (1 - x**51)/(1 - x)

print("Computational error: ", y - horner(expr, n, x))
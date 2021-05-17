import numpy as np
import sys
matrix = np.zeros([100, 100])
counter = 0

# Answers
solution = []
back = []
for i in matrix:
	solution.append(0)
	back.append(0)

solution[0] = 1

# Making the matrix
for i in matrix:
	matrix[counter][counter] = 2
	if counter == 99:
		break
	matrix[counter][counter+1] = -1
	matrix[counter+1][counter] = -1
	counter += 1


print("Tri-diagonal matrix:\n")
print(matrix)
print("B vector matrix:\n")
print(solution)

# Gaussian Elimination
n = counter + 1
for i in range(n):
	#print(i)
	if matrix[i][i] == 0:
		sys.exit('Divide by zero detected!')
	for j in range(i+1, n):
		c = matrix[j][i] / matrix[i][i]
		if i != 99:
			if c != 0:
				solution[i+1] = solution[i] * np.abs(c)
		for k in range (n):
			matrix[j][k] = matrix[j][k] - c * matrix[i][k]


print("Matrix after Gaussian Elimination:\n")
print(matrix)
print("B vector after Gaussian Elimination:\n")
print(solution)

# Back Substitution
solution.reverse()
back[0] = solution[0]/matrix[99][99]
for i in range(99):
	back[i+1] = (solution[i+1] - (back[i]*matrix[98-i][99-i])) / matrix[98-i][98-i]

print("First 5 solutions in form: [x5, x4, x3, x2, x1]")
print(back[95:100])

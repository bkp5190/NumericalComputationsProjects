import numpy as np
import matplotlib.pyplot as plt

#Given function
def F(x):
    output = (4 / np.pi) * (1 / (1 + x**2))
    return output

#Composite Trapezoidal Rule for integration
def Trap(values):
    h = np.abs(values[0][0] - values[1][0])
    sum_y = 0
    compTrapRuleFront = (h / 2) * (values[0][1] + values[len(values)-1][1])
    for i in range(len(values)):
        sum_y += values[i][1]
    compTrapRuleBack = h * sum_y
    return (compTrapRuleFront + compTrapRuleBack)


#Simpson's Composite Rule for integration
def Simpsons(values):
    sum_s = 0
    sum_b = 0
    h = np.abs(values[0][0] - values[1][0])
    simpCompRuleFront = (h / 3) * (values[0][1] + values[len(values) - 1][1])
    for i in range(len(values)):
        if np.abs(i % 2) == 1:
            sum_s += values[i][1]
        else:
            sum_b += values[i][1]
    simpCompRuleMid = sum_s * ((4 * h) / 3)
    simpCompRuleBack = sum_b * ((2 * h) / 3)
    return (simpCompRuleFront + simpCompRuleMid + simpCompRuleBack)

#Composite Mid-point Rule for integration
def Mid(values):
    h = np.abs(values[0][0] - values[1][0])
    sum_m = 0
    for i in range(len(values)):
        sum_m += (values[i][1] + (h/2))
    midpoint = h * sum_m
    return (midpoint)

#Calculates the new values and puts them in a list for the new function before calling the integration functions to find the final integration values
def Integration(n):
    IntValues = []
    counter = 1/n
    for j in np.arange(0, 1+counter, counter):
        xvalue = j
        yvalue = F(j)
        IntValues.append([xvalue, yvalue])
    ansTrap = Trap(IntValues)
    ansSimp = Simpsons(IntValues)
    ansMid = Mid(IntValues)
    return ansTrap, ansSimp, ansMid

ansTrap = np.zeros(3)
ansSimp = np.zeros(3)
ansMid = np.zeros(3)
ansTrapError = np.zeros(3)
ansSimpError = np.zeros(3)
ansMidError = np.zeros(3)
x_vals = []
y_vals = []
nvalues = [4,8,16]
for i in nvalues:
    ansTrap[nvalues.index(i)], ansSimp[nvalues.index(i)], ansMid[nvalues.index(i)] = Integration(i)
    ansTrapError[nvalues.index(i)] = np.abs(1 - ansTrap[nvalues.index(i)])
    ansSimpError[nvalues.index(i)] = np.abs(1 - ansSimp[nvalues.index(i)])
    ansMidError[nvalues.index(i)] = np.abs(1 - ansMid[nvalues.index(i)])
    x_vals.append(i)
    y_vals.append(1)


#Plotting
plt.plot(x_vals,y_vals, label='Actual Value = 1')
plt.plot(x_vals,ansTrap, label='Trapezoidal Integration')
plt.plot(x_vals,ansSimp, label='Simpson Integration')
plt.plot(x_vals,ansMid, label='Midpoint Integration')
plt.scatter(x_vals,y_vals)
plt.scatter(x_vals,ansTrap)
plt.scatter(x_vals,ansSimp)
plt.scatter(x_vals,ansMid)
plt.legend()


plt.show()
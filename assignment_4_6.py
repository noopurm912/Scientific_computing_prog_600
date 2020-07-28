# assignment_4_6.py

import numpy as np
import math

def taylor(dfdx, n, xi, h, start=0):
    sum = 0
    for i in range(start, n + 1):  # loop from i=start to n
        sum += dfdx(i, xi) * h ** i / math.factorial(i)
    # end for
    return sum

def f(x):
    return np.log(x)

def dfdx(i, x):
    return {0: f(x),
            1: 1/x,
            2: -(1/(x**2)),
            3: 2/(x**3),
            4: -(6/(x**4))}.get(i, 0)

xi = 1   # base point xi
x = 2.5  # xiplus1 (x value in approximation f(x)
h = x - xi

tv = f(xi + h)  # compare true value from known f(x = xi+h)
print(f'True Value = {tv:.4}')

for i in range(0, 5):
    av = taylor(dfdx, i, xi , h)
    et = abs(1 - av/tv)  #compute true relative error
    print(f'{i} order: Approximate value = {av} True Relative Error = {et:.2%}')
# end for
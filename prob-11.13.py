#Problem 11.13
#author: Luis Paris
#solve equations using LU decomposition

import numpy as np
import _linalg4

A = np.array([
    [-8, 1, -2],
    [-3, -1, 7],
    [2, -6, -1],
])

b = np.array([
    -20,
    -34,
    -38,
])

print("A = \n{}".format(np.array(A)))
print("b = {}\n".format(np.array(b)))

x = _linalg4.gausseidel(A, b)
print("(gauss-seidel)\nx = {}".format(x))



#Problem 10.6
#prob-10.6.py

# To compute LU decomposition

import numpy as np
import _linalg2

A = [[10, 2, -1],
     [-3, -6, 2],
     [1, 1, 5]]

L, U = _linalg2.decompLU(A)
print('L =\n{}'.format(L))
print('U =\n{}'.format(U))



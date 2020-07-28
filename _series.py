# _series.py
import math


def taylor(dfdx, n, xi, h, start=0):
    sum = 0
    for i in range(start, n + 1):  # loop from i=start to n
        sum += dfdx(i, xi) * h ** i / math.factorial(i)
    # end for
    return sum


# end taylor()

def R(dfdx, n, xi, h):
    pass

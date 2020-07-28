# Open Methods
# Problem 6.9

import math
import _plot, prob6_9_roots2

# function f(X) = f(x) = x3 – 6x2 + 11x – 6.1
def f(x): return x**3 - 6*x**2 + 11*x - 6.1

# graphical method

_plot.graph(f, xl=0.5, xu=3.5)
# visual inspection reveals that root lies between 3.0 and 3.5

_plot.graph(f, xl=3.0, xu=3.5)
# visual inspection reveals that root is approx.. 3.047

# Newton-Raphson Method
print("\nNewton-Raphson Method:")
def df(x): return 3*x**2 - 12*x + 11
prob6_9_roots2.newton(f, df, x0=3.5, debug=True)

# Secant Method
print("\nSecant method:")
prob6_9_roots2.secant(f, x0=2.5, x1=3.5, debug=True)

# modified Secant Method
print("\nModified Secant Method:")
prob6_9_roots2.modified_secant(f, x0=3.5, debug=True)
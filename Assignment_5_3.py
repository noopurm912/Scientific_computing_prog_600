# Bracketing Method
# Excercise 5.3

import math
import _plot, prob5_3_roots


# function f(X) = – 25 + 82x – 90x2 + 44x3 – 8x4 + 0.7x5
def f(x): return -25 + 82 * x - 90 * x ** 2 + 44 * x ** 3 - 8 * x ** 4 + 0.7 * x ** 5

#graphical method

_plot.graph(f, xl=0.5, xu=1.0)
# visual inspection reveals that root lies between 0.5 and 0.6

_plot.graph(f, xl=0.5, xu=0.6)
# visual inspection reveals that root is approx 0.5794

print("Bisection Method: ")
xr_b = prob5_3_roots.bisect(f, xl = .5, xu = 1.0, debug = True)
print(f"The Root Using Bisection method is : {xr_b} ")

print("========================================================")

print("False Position Method: ")
xr_f = prob5_3_roots.falsepos(f, xl = .5, xu = 1.0, debug = True)
print(f"The Root Using False Position method is : {xr_f:.4}")

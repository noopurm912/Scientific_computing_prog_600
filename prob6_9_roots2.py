'''
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on open methods for root finding
- implemented from algorithms/pseudocode provided
'''
'''
module: prob6_9_roots2.py
- updated Newton-Raphson method 
- to get the value of the function f(X) = f(x) = x3 – 6x2 + 11x – 6.1 with each value of
  xr to check whether it's close to zero or not 
- limit the iteration to 3.
'''


def newton(f, df, x0, es100=.5, imax=3, debug=False):
    x0 = float(x0)
    iter = 1
    while True:
        xr = x0 - f(x0) / df(x0)
        if xr: ea = abs(1 - x0 / xr)
        if debug: print(f'iteration={iter}, x0={x0:.4f}, xr={xr:.4f}, ea={ea:.4%}, function_value={f(xr):.4}')
        if ea * 100 < es100 or iter >= imax:
            break
        iter += 1
        x0 = xr
    # end while
    return xr


# end newton()

# Secant Method (three iterations)
def secant(f, x0, x1, es100=.5, imax=3, debug=False):
    x0 = float(x0)
    x1 = float(x1)
    iter = 1
    while True:
        xr = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
        if xr: ea = abs(1 - x1 / xr)
        if debug: print(
            f'iteration={iter}, x0={x0:.4f}, x1={x1:.4f}, xr={xr:.4f}, ea={ea:.4%}, function_value={f(xr):.4}')
        if ea * 100 < es100 or iter >= imax:
            break
        iter += 1
        x0 = x1
        x1 = xr
    # end while
    return xr


# end secant()


# modified secant method (three iterations, xi 5 3.5, d 5 0.01) and  p_f is a small perturbation fraction
def modified_secant(f, x0, es100=.5, imax=3, p_f=0.01, debug=False):
    x0 = float(x0)
    iter = 1
    while True:
        xr = x0 - (p_f * x0 * f(x0) / (f(x0 + p_f * x0) - f(x0)))
        if xr: ea = abs(1 - x0 / xr)
        if debug: print(f'iteration={iter}, x0={x0:.4f}, xr={xr:.4f}, ea={ea:.4%}, function_value={f(xr):.4}')
        if ea * 100 < es100 or iter >= imax:
            break
        iter += 1
        x0 = xr
    # end while
    return xr
# end modified_secant()

#_polyroots_muller.py

import math, numpy as np, cmath


def quadratic(a, b, c):
    """returns the two roots for quadratic equation a*x**2 + b*x + c"""
    disc = b*b - 4*a*c
    irad = cmath.sqrt(disc)
    if abs(irad.imag) < 1e-6:
        rad = irad.real
    else:
        rad = irad
    d1 = b + rad
    d2 = b - rad
    xr1 = -2*c / (d1 if abs(d1) > abs(d2) else d2)
    xr2 = -2 * c / (d2 if abs(d1) > abs(d2) else d1)
    return xr1, xr2
# end Quadratic

def muller(f, xr, h, es100=.5, imax=1000, debug=False):
    x2 = float(xr)
    x1 = float(xr + h * xr)
    x0 = float(xr - h * xr)
    iter = 0
    ea = 1.  # 100%
    while True:

        if debug:
            print(f'iter={iter}, x0={x0:.2f}, x1={x1:.2f}, x2={x2:.2f}, xr={xr:.2f}, ea={ea:.2%}')
        if ea * 100 < es100 or iter > imax:
            break
        iter += 1
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f(x1) - f(x0)) / h0
        d1 = (f(x2) - f(x1)) / h1
        a = (d1 - d0) / (h1 + h0)
        dxr, _ = quadratic(a, b=a * h1 + d1, c=f(x2))
        xr = x2 + dxr
        if xr: ea = abs(dxr / xr)
        x0, x1, x2 = x1, x2, xr
    # end while
    return xr
# end muller()

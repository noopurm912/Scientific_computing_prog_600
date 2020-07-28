# prob5_3_roots.py
# 5_3_bisect_method

def bisect(f, xl, xu, es100=10, imax=1000, debug = False):
    xl, xu = float(xl), float(xu)
    ea = 1.0 # assume 100% relative error
    x0 = xl
    iter = 0
    while True:
        xr = (xl + xu) / 2
        iter += 1
        if xr: ea = abs(1 - x0/xr)
        if debug:
            print(f'Iteration={iter}, xl={xl}, xu={xu}, xr={xr}, ea={ea:%}')
        test = f(xl) * f(xr)
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0
        if ea*100 < es100 or iter >= imax:
            break
        x0 = xr
    # end while
    return xr
# end bisect


def falsepos(f, xl, xu, es100=0.2, imax=100, debug=False):
    xl, xu = float(xl), float(xu)
    ea = 1.0  # assume 100% relative error
    x0 = xl
    iter = 0
    while True:
        xr = xl - ((xu - xl) * f(xl) / (f(xu) - f(xl)))
        iter += 1
        if xr: ea = abs(1 - x0 / xr)
        if debug:
            print(f'Iteration={iter}, xl={xl}, xu={xu:.4}, xr={xr:.4}, ea={ea:%}')
        test = f(xl) * f(xr)
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0
        if ea * 100 < es100 or iter >= imax:
            break
        x0 = xr
    # end while
    return xr
# end falsepos


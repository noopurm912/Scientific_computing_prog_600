# script: ex-bairstow-poly3.py
# bairstow's method
# 3. f(x) = -2 + 6.2x - 4x2 + 0.7x3

import matplotlib.pyplot as plt
import _plot, _poly, _polyroots2_bairstow

# a = [-2, 6.2, -4, 0.7]

def f(x): return _poly.eval(a, x)  # evaluate polynomial a as a function

xl, xu = -5, 5
_plot.graph(f, xl, xu, title="y = {}".format(_poly.tostr(a)))

prec = 4

xr1, xr2 = _polyroots2_bairstow.bairstow(a, r=1, s=1, es100=.5 * 10 ** (2 - prec), debug=True, tab=11, precision=prec)
print("xr1 = {:.{p}}\nxr2 = {:.{p}}".format(xr1, xr2, p=prec))

# plot roots
xr = [xr1, xr2]  # add additional roots here
_plot.graph(f, xl, xu, title="y = {}".format(_poly.tostr(a)), show=False)
axes = plt.gca()  # get current axes object and obtain dimensions
left, right = axes.get_xlim();
width = right - left
down, up = axes.get_ylim();
height = up - down
for i in range(len(xr)):
    plt.annotate("xr{} = {:.{p}}".format(i + 1, xr[i], p=prec),
                 xy=(xr[i].real, 0), xytext=(xr[i].real + width / 25, (i + 1) * height / 25),
                 arrowprops=dict(width=.25, headwidth=4, headlength=9))
plt.show()

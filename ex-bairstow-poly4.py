# script: ex-bairstow-poly4.py
# bairstow's method


import matplotlib.pyplot as plt
import _plot, _poly, _polyroots2_bairstow

# 4. f(x) = x4 - 2x3 + 6x2 - 2x + 5
a = [5, -2, 6, -2, 1]



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

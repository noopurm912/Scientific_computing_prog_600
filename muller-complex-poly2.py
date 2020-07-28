# muller-complex-poly2.py

import matplotlib.pyplot as plt
import _poly, _plot, _polyroots_muller

# 2. f(x) = 2x4 + 6x2 + 8      xr = 1 h = .5

a = [8, 0, 6, 0, 2]

def f(x): return _poly.eval(a, x)

# Graphical Solution
xl, xu = -5, 5
# _plot.graph(f, xl, xu)
_plot.graph(f, xl, xu, title='y = {}'.format(_poly.tostr(a)))

#  Muller Method
xr1 = _polyroots_muller.muller(f, xr=1, h=.5, debug=True)
print('\nxr1 = {:.2f}'.format(xr1))

b, _ = _poly.defl(a, xr1)

xr2, xr3 = _polyroots_muller.quadratic(a=b[2], b=b[1], c=b[0])
print(f"xr2 = {xr2:.2}")
print(f"xr3 = {xr3:.2}")

# plot roots
xr = [xr1, xr2, xr3]
_plot.graph(f, xl, xu, title="y = {}".format(_poly.tostr(a)), show=False)
axes = plt.gca()  # get current axes object and obtain dimensions
left, right = axes.get_xlim();
width = right - left
down, up = axes.get_ylim();
height = up - down
for i in range(len(xr)):
    plt.annotate(f"xr{i + 1} = {xr[i]:.{2}}", xy=(xr[i].real, 0),
                 xytext=[xr[i].real + width / 25, (i + 1) * height / 25],
                 arrowprops=dict(width=.25, headwidth=4, headlength=9))
plt.show()

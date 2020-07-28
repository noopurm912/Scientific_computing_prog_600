#ex-muller-7.2-conjugate-todo.py

import matplotlib.pyplot as plt
import _poly, _plot, _polyroots_muller
#f(x) = 2x4 + 6x2 + 8
#x**3 - 13*x - 12
a = [-2, 2, -1, 1]
#a = [-12, -13, 0, 1]
def f(x): return _poly.eval(a, x)

xl, xu = -5, 5
_plot.graph(f, xl, xu, title='y = {}'.format(_poly.tostr(a)))

#change initial root estimate to xr=-4 so muller's parabola curvefits below x axis (returning a complex root)
xr1 = _polyroots_muller.muller(f, xr=1, h=.5, debug=True)
print('\nxr1 = {:.4f}'.format(xr1))

#root is imaginary, so create conjugate xr2 and deflate by (x - xr1)(x - xr2)
xr2 = complex(xr1.real, -xr1.imag)  #create conjugate
print("xr2 = {:.4f}  (obtained from conjugate)".format(xr2))
b = _poly.div(a, [(xr1*xr2).real, -(xr1+xr2).real, 1])[0]  #deplete by (x - xr1)(x - xr2)

#solve remaining monomial
xr3 = - b[0] / b[1]
print('xr3 = {:.4f}'.format(xr3))

#plot roots
xr = [xr1, xr2, xr3]
_plot.graph(f, xl, xu, title="y = {}".format(_poly.tostr(a)), show=False)
axes = plt.gca()  #get current axes object and obtain dimensions
left, right = axes.get_xlim(); width = right - left
down, up = axes.get_ylim(); height = up - down
for i in range(len(xr)):
    plt.annotate("xr{} = {:.{p}}".format(i+1, xr[i], p=4),
                 xy=(xr[i].real, 0), xytext=(xr[i].real + width/25, (i+1)*height/25),
                 arrowprops=dict(width=.25, headwidth=4, headlength=9))
plt.show()

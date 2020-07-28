# assignment_4_4.py
import math


def arc_tan(x, it):
    arc_tan_sum = 0
    for i in range(0, it):
        arc_tan_sum += ((-1) ** i) * ((x ** (2 * i + 1)) / (2 * i + 1))
    return arc_tan_sum
# end arc_tan()

# initializations

n = 2  # 2 significant figures
es100 = 0.5 * 10 ** (2 - n)  # error tolerance
x = math.pi / 6  # reference point x
tv = math.atan(math.pi / 6)

print(f'True Value = {tv:.7}')
print(f'es = {es100}\n')

# main program
avold = 0
iteration = 0

while True:
    iteration += 1
    av = arc_tan(x, iteration)  # approximate value
    ea = 1 - avold / av
    et = 1 - av / tv  # true relative error
    print(f'iteration = {iteration}, True Value = {tv:.7}, Approximate Value = {av:.7}, et = {et:.4%}, ea={ea:.4%}')
    avold = av
    if abs(ea) * 100 < es100:
        break
# end while

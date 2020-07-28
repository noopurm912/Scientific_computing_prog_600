# assignment_3_10.py
import math


def cos_func(x, n):
    cos_sum = 0
    for i in range(0, n):
        cos_sign = (-1) ** i
        cos_sum += cos_sign * ((x ** (2 * i)) / math.factorial(2 * i))

    return cos_sum


# end cos_func()

# initializations

n = 8  # 8 significant figures
es100 = 0.5 * 10 ** (2 - n)  # error tolerance
x = 0.3 * math.pi  # reference point x
tv = math.cos(0.3 * math.pi)
print(f'True Value = {tv:.8}')
print(f'es = {es100}\n')

# main program
avold = 0
iteration = 0

while True:
    iteration += 1
    av = cos_func(x, iteration)  # approximate value
    ea = 1 - avold / av
    et = 1 - av / tv  # true relative error
    print(f'iteration = {iteration}, True Value = {tv:.10}, Approximate Value = {av:.8}, et = {et:.8%}, ea={ea:.8%}')
    avold = av
    if abs(ea) * 100 < es100:
        break
# end while


import numpy as np
a = np.array([[10, 2, -1], [-3, -6, 2], [1, 1, 5]])
b = np.array([[.11072, .038083, 0.007], [-0.0588, -0.1764, 0.0593], [-0.0104, 0.02803, 0.1886]])
c = a.dot(b)
np.set_printoptions(suppress=True)
print(c)
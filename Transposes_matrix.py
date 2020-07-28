# transpose_matrix.py

import numpy as np


def transpose_matrix():
    r = int(input("Enter the number of rows:"))
    c = int(input("Enter the number of columns:"))
    print("Enter the elements in same line with space(row-wise): ")
    a = list(map(int, input().split()))
    m = np.array(a).reshape(r, c)
    print("The matrix is: ")
    print(m)
    print("The Transpose of the Matrix: ")
    print(np.transpose(m))
    x = input("do you want to test for other matrix?: y/n: ")
    if x == 'y':
        transpose_matrix()
    else:
        exit()

transpose_matrix()

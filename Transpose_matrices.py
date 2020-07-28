# Transpose_matrices.py

def transpose_matrices():
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))

    # Matrix Initialization
    m = []
    print("Enter the elements row-wise:")

    for i in range(r):
        a = []
        for j in range(c):
            a.append(float(input()))
        m.append(a)

    for i in range(r):
        for j in range(c):
            print(m[i][j], end=" ")
        print()

    # printing Transpose of the matrix

    print("The transpose of matrix : ")
    result = map(list, zip(*m))
    for r in result:
        print(r)

transpose_matrices()
x = input("do you want to test for other matrix?: y/n: ")
if x == 'y':
    transpose_matrices()
else:
    exit()

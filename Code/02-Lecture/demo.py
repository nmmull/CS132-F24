from sympy import *

B = Matrix([
    [2, 3, -6],
    [4, -5, 10]
])

B[1,:] = B[1,:] - 2 * B[0,:]
B[1,:] /= -11
B[0,:] -= 3 * B[1,:]
B[0,:] /= 2

B[0,:], B[1,:] = B[1,:], B[0,:]

pprint(B)

A = Matrix([
    [1, 2, 0, 1],
    [-1, -1, -1, -1],
    [2, 6, -1, 1]
])

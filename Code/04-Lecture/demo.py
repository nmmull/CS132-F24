import numpy as np
from sympy import *

# An implementation of Gaussian elimination for 2 by 2 matrices
def gauss_small(A):
    A[1,:] -= A[1, 0] / A[0, 0] * A[0,:]
    if not np.isclose(A[1,1], 0):
        A[1,:] /= A[1, 1]
        A[0,:] -= A[0, 1] * A[1,:]
        A[0,:] /= A[0, 0]
    else:
        A[1, 1] = 0

# carfully chosen very large number
c = 100000000000000010241

# NumPy matrix for an inconsistent system
B = np.array([
    [1, c, 2],
    [1, c, 3]
])

B[0, 1] = B[0, 1] / 7 / 10 * 7
B[1, 1] = B[1, 1] / 10

gauss_small(B)
print()
print("Solving Ill-conditioned problem with NumPy (gives wrong solution):")
print()
print(B)

# SymPy matrix for an inconsistent system
C = Matrix([
    [1, c, 2],
    [1, c, 3]
])

C[0, 1] = C[0, 1] / 7 / 10 * 7
C[1, 1] = C[1, 1] / 10

print()
print("Solving Ill-conditioned problem in SymPy (gives correct solution):")
print()
pprint(C.rref()[0])

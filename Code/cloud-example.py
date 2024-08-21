import sympy as sp
from sympy.matrices import Matrix

A = Matrix([
  [35000, 24000, 10000, 439000],
  [90000, 13000, 21000, 813000],
  [41000, 19000, 34000, 571000]])

sp.pprint(A.rref()[0])


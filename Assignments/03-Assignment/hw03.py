from matlib import *
from numpy import isclose

v = Vector([1.,2.,3.], 3)

def vec_scale(val, vec):
    out = []
    for i in range(vec.num_entries):
        out.append(val * vec.get_entry(i))
    return Vector(out, vec.num_entries)

w = Vector([2.,4.,6.], 3)
assert(vec_scale(2.0, v).equals(w))

w = Vector([-1.,-2.,-3.], 3)
assert(vec_scale(-1.0, v).equals(w))

def vec_add(v1, v2):
    if v1.num_entries != v2.num_entries:
        raise Exception("DIMENSION MISMATCH")
    else:
        entries = []
        for i in range(v1.num_entries):
            entries.append(v1.get_entry(i) + v2.get_entry(i))
        return Vector(entries, v1.num_entries)

w = Vector([2.,4.,6.], 3)
assert(vec_add(v, v).equals(w))

u = Vector([4.,5.,6.], 3)
w = Vector([5.,7.,9.], 3)
assert(vec_add(v, u).equals(w))

def vec_inner(v1, v2):
    if v1.num_entries != v2.num_entries:
        raise Exception("DIMENSION MISMATCH")
    out = 0.0
    for i in range(v1.num_entries):
        out += v1.get_entry(i) * v2.get_entry(i)
    return out

u = Vector([4.,5.,6.], 3)
assert(isclose(vec_inner(v, u), 32.))

def mat_vec_mul(a, v):
    if a.cols != v.num_entries:
        raise Exception("DIMENSION MISMATCH")
    out = Vector([0. for _ in range(a.rows)], a.rows)
    for j in range(a.cols):
        out = vec_add(out, vec_scale(v.get_entry(j), a.get_col(j)))
    return out

a = Matrix([
    [1.,2.,3.],
    [4.,5.,6.],
    [7.,8.,9.]
], 3, 3)
v = Vector([1.,2.,3.], 3)
w = Vector([14., 32., 50.], 3)
assert(mat_vec_mul(a, v).equals(w))

# def mat_vec_mul2(a, v):
#     if a.cols != v.num_entries:
#         raise Exception("Dimensions don't match")
#     out = []
#     for i in range (a.rows):
#         out.append(vec_inner(a.get_row(i), v))
#     return Vector(out, v.num_entries)

# assert(mat_vec_mul2(a, v).equals(w))

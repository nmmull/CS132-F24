import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve
import time

def test_matrix(k):
    n = 2 * k
    d = 4 * np.eye(n)
    d -= np.eye(n, k=2) + np.eye(n, k=-2)
    a = [-1 * (n % 2) for n in range(1, n)]
    d += np.diag(a, k=-1) + np.diag(a, k=1)
    return d

# n = 10 ** 3
# print("building test matrix...")
# m = test_matrix(n)

# start_time = time.time()
# print("factoring m...")
# factors = lu_factor(m)
# print(f'time: {time.time() - start_time} seconds')

# start_time = time.time()
# print("solving with LU...")
# for _ in range(100):
#     lu_solve(factors, np.random.rand(2 * n))
# print(f'time: {time.time() - start_time} seconds')

# start_time = time.time()
# print("inverting m...")
# m_inv = np.linalg.inv(m)
# print(f'time: {time.time() - start_time} seconds')

# start_time = time.time()
# print("solving with inv...")
# for _ in range(100):
#     m_inv @ np.random.rand(2 * n)
# print(f'time: {time.time() - start_time} seconds')

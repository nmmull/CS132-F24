import numpy as np

a0 = np.vstack([-3 * np.eye(9), np.zeros((2, 9))])

a1 = np.eye(10, 10, -1)

a2 = np.hstack([5 * np.ones((5, 4)), np.eye(5)])

a3 = np.vstack([np.hstack([np.arange(10).reshape((5, 2)), -1 * np.ones((5, 5))]), \
                np.hstack([2 * np.ones((3, 4)), np.eye(3)])])

a4 = np.diag([i + 1 for i in range(10)]) + np.diag([i + 1 for i in range(10)])[::-1]

a5 = np.tril(2 * np.ones((7, 7)), -1) + np.triu(3 * np.ones((7, 7)), 1)

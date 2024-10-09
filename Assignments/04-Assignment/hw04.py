import numpy as np
from scipy.linalg import lu

def fwd_elim(a):
    """forward elimination step from Gaussian elimination"""
    # DON'T WORRY ABOUT THIS IMPLEMENTATION
    return lu(a)[2]

def is_con_aug(a):
    """checks if an augmented matrix is consistent

    parameters:

    A: 2D numpy array representing an augmented matrix

    returns:

    True if A represents the augmented matrix of a consistent system
    of linear equations, and False otherwise.

    """
    e = fwd_elim(a)
    for row in e:
        if np.nonzero(row)[0][0] == e.shape[1] - 1:
            return False
    return True

def np_array_to_col(v):
    return np.atleast_2d(v).T

def is_con_mat_eq(a, b):
    """checks if a matrix equation is consistent

    parameters:

    A: 2D numpy array
    b: 1D numpy array

    returns:

    True if Ax = b is consistent, and False otherwise.

    """
    return is_con_aug(np.hstack((a, np_array_to_col(b))))

def in_span(v, a):
    """checks if a vector is in the span of a list of vectors

    parameters:

    u: 1D numpy array
    A: 2D numpy array

    returns:

    True if u lies in the span of the columns of A.

    """
    return is_con_mat_eq(a, v)

def num_pivots(a):
    """returns the number of pivot positions in a matrix

    parameters:

    A: 2D numpy array

    returns:

    the number of pivot positions of A

    """
    a = fwd_elim(a)
    return sum(map(lambda x: len(np.nonzero(x)[0]) != 0, list(a)))

def full_span(a):
    """checks if the columns of a matrix have full span

    parameters:

    A: 2D numpy array

    returns:

    True if the columns of A span all of Rn, given that A has n rows,
    and False otherwise

    """
    return num_pivots(a) == a.shape[0]

def lin_ind(a):
    """checks if the columns of a matrix are linearly independent

    parameters:

    A: 2D numpy array

    returns:

    True if the columns of A are linearly independent, and False
    otherwise

    """
    return num_pivots(a) == a.shape[1]

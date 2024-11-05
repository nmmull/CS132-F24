import networkx as nx
import numpy as np

def at_least_k_steps_matrix(adj_mat, k):
    """computes the matrix which expresses reachability in at least k
    steps

    Paramters:

    adj_mat: 2D numpy array (an adjacency matrix for a SIMPLE graph)

    k: nonnegative integer

    Returns:

    (adj_mat + I)^k

    the matrix whose (i, j)th entry is the number of paths from v_i to
    v_j in at most `k` steps

    """
    id_mat = np.eye(adj_mat.shape[0])
    return np.linalg.matrix_power(adj_mat + id_mat, k)

def reach(a, j):
    """computes the number of nodes reachable from v_j

    Parameters:

    a: 2D numpy array (the output of at_least_k_steps_matrix(adj_mat, k))

    j: integer where (0 <= j < a.shape[1])

    Returns:

    We say that the k-REACH of a vertex v is the number of vertices
    which can be reached from v in at most k steps.  This functions
    returns the k-reach of a vertex v in the graph with adjacency
    matrix adj_mat, given the matrix (adj_mat + I)^k, the output of
    at_least_k_steps_matrix(adj_mat, k).

    Note that this is the same as the number of NONZERO values in the
    `j`th column of the input matrix `a`.

    """
    return len(np.nonzero(a[:,j])[0])

def max_reach(a):
    """computes the maximum reach for any node

    Parameters:

    a: 2D numpy array (the output of at_least_k_steps_matrix(adj_mat, k))

    Returns:

    max{reach(a, j) : 0 <= j < a.shape[1]}

    the maxmimum reach of any node

    """
    max_r = -1
    for j in range(a.shape[1]):
        max_r = max(reach(a, j), max_r)
    return max_r

def doesnt_have_max_reach(a):
    """computes the list of indices which do not have maximum reach

    Parameters:

    a: 2D numpy array (the output of at_least_k_steps_matrix(adj_mat, k))

    Returns:

    the list of indices of vertices which don't have maximum reach,
    i.e., the list of indices i such that reach(a, i) < max_reach(a)

    """
    out = []
    max_r = max_reach(a)
    for j in range(a.shape[1]):
        if reach(a, j) < max_r:
            out.append(j)
    return out


"""There was a film that came out a couple years ago which received a
0% on Rotten Tomatoes, but was despite this quite popular (I'll let
you determine why).  It turns out every actor in our dataset is within
SEVEN degrees of each other, EXCEPT TWO, who were co-stars in the
aformentioned film.  In the variable `disconnected`, write down the
list of names (as strings) of these two actors.  IMPORTANT: you should
not be computing these values in this file, just writing them down.
You should do your work in `costar.py` to figure out the names.

"""
disconnected = ['Anna Maria Sieklucka', 'Michele Morrone']

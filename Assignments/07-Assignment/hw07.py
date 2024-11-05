import numpy as np
import sys

def to_stochastic(words, pairs):
    """makes a stochastic matrix from a collection of word pairs

    Parameters:

    words: list of strings
    pairs: list of pairs of strings from WORDS

    Returns:

    a 2D numpy array A such that

              number of occurrences of (WORDS[j], WORDS[i]) in PAIRS
    A[i, j] = ---------------------------------------------------------
              number of occurrences of (WORDS[j], w) in PAIRS for any w

    """
    n = len(words)
    out = np.zeros((n, n))
    for (w1, w2) in pairs:
        i1 = words.index(w1)
        i2 = words.index(w2)
        out[i2, i1] += 1
    for i in range(n):
        div = np.sum(out[:,i])
        if div != 0:
            out[:,i] /= div
    return out

def random_step(a, i):
    """performs a single random step given a stochastic matrix

    Parameters:

    a: 2D numpy array
    i: int, starting node

    Returns

    An int which is one step away from I, chosen according to the
    distribution given by A

    """
    rng = np.random.default_rng()
    return rng.choice(a.shape[0], p=a[:, i])

def random_walk(a, i, length):
    """performs a random walk

    Parameters:

    a: 2D numpy array, representing a (square) stochastic matrix
    i: int, index of columns
    length: int, the number of steps (i.e., edges) of the random walk

    Returns:

    A list of indicies of length LENGTH, resulting from a random walk
    on A starting at I

    """
    walk = [i]
    next_index = i
    for _ in range(length):
        next_index = random_step(a, next_index)
        walk.append(next_index)
    return walk

# read in txt file at stdin and split into words
try:
    text_file = open('sonnets.txt', 'r', encoding='utf-8')
except:
    print("Make sure sonnets.txt is in the same directory as hw07.py")
    exit()
text = text_file.read()[1:].split()
# delete duplicates
words = list(dict.fromkeys(text))
# pairs of adjacent words
pairs = list(zip(text[:-1], text[1:]))

# make stocastic matrix
a = to_stochastic(words, pairs)

# perform a random walk on the matrix
walk = random_walk(a, 0, 15*6 - 1)
# make a list of words from the random walk
gen_text = np.array(list(map(lambda i: words[i], walk)))

# minor formatting
gen_text.shape = (15, 6)
poem = "\n".join([" ".join(row) for row in gen_text]).lower()
if not poem[-1].isalpha():
    poem = poem[:-1]

print()
print(poem + "...")
print()

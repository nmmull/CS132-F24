import numpy as np
from numpy.linalg import norm

def similarity(word_vecs, w1, w2):
    """Determines the similarity of two words

    Parameters

      word_vecs: dictionary mapping strings (words) to numpy arrays
      w1: string (word)
      w2: string (word)

    Returns

      The cosine similarity of the vectors in `word_vecs` representing
      the words `w1` and `w2`

    Notes

      You should use numpy.dot and numpy.linalg.norm

    """
    v1 = word_vecs[w1]
    v2 = word_vecs[w2]
    return np.dot(v1, v2) / (norm(v1) * norm(v2))

def most_similar_words(word_vecs, n, word):
    """Determines the closest words to a given word

    Parameters

      word_vecs: dictionary mapping strings (words) to numpy arrays
      n : nonnegative int
      word : string (word)

    Returns

      A list of word-float pairs given of length `n` (you may assume
      that `n` is smaller than the number of keys `word_vecs`) which
      contains the `n` closest words to `w`, not including `w`, in
      order of decreasing similarity.

    """
    def insert(out, p):
        for i in range(len(out) + 1):
            if i == len(out) or p[1] > out[i][1]:
                out.insert(i, p)
                break
        if len(out) == n + 1:
            out.pop(-1)

    def worst(out):
        if len(out) == 0:
            return -1.
        return out[-1][1]

    out = []
    for (w, v) in word_vecs.items():
        if w != word:
            s = similarity(word_vecs, w, word)
            if s > worst(out):
                insert(out, (w, s))
    return out

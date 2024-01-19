import numpy as np

def entropy(px):
    return -np.sum(px * np.log2(px))
     
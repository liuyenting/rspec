import numpy as np

from .candidates import find_candidates

def lstsq(mix_spec, database):
    """
    Return percentage of candidate spectrum.
    """
    names, A = find_candidates(spectrum, database)
    y = mix_spec['intensity'].values

    # reshape to satisfy the array condition
    A = A.T
    y = y[n.newaxis].T

    coefs, res, _, _ = np.linalg.lstsq(A, y, rcond=None)
    den = np.sum(coefs)
    coefs /= den

    return names, coefs
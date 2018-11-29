import numpy as np

def find_candidates(spectrum, database):
    """
    Notes
    -----
    - Spectrum is not used for now.
    """
    # pull all the spectrum in the database
    data = zip(*[(k, v['intensity'].values) for k, v in database.items()])
    return data[0], np.vstack(data[1])
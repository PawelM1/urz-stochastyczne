# custom distributions
from scipy import stats
class your_distribution(stats.rv_continuous):
    def _pdf(self, x):
        return ( sin(x) ** (-0.75) ) / (4.32141 * (x ** (1/5)))

distribution = your_distribution()
distribution.rvs()



#######################

# Without using scipy and given a numerical sampling of your PDF,
# you can sample using a cumulative distribution and linear interpolation.
# The code below assumes equal spacing in x. It could be modified to do an
# integration for an arbitrarily sampled PDF. Note it renormalises
# the PDF to 1 within the range of x.

import numpy as np

def randdist(x, pdf, nvals):
    """Produce nvals random samples from pdf(x), assuming constant spacing in x."""

    # get cumulative distribution from 0 to 1
    cumpdf = np.cumsum(pdf)
    cumpdf *= 1/cumpdf[-1]

    # input random values
    randv = np.random.uniform(size=nvals)

    # find where random values would go
    idx1 = np.searchsorted(cumpdf, randv)
    # get previous value, avoiding division by zero below
    idx0 = np.where(idx1==0, 0, idx1-1)
    idx1[idx0==0] = 1

    # do linear interpolation in x
    frac1 = (randv - cumpdf[idx0]) / (cumpdf[idx1] - cumpdf[idx0])
    randdist = x[idx0]*(1-frac1) + x[idx1]*frac1

    return randdist


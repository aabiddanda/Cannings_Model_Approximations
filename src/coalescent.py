
'''
    Computing Genealogical Properties under the Coalescent
        (Sort of like a lib module for most Coalescent computations)
'''

import numpy as np


# TODO : set up some sort of epochs example here

'''
    Function to precompute some values for the sums
    NOTE : factors are only for the expectation (but can be done for the variance as well)
'''
def precompute(n):
    factors = [0.0 for i in range(n+1)]
    p = 1.0
    for i in range(1, n+1):
        p *= 1.0 * (n - i + 1) / (n + i - 1)
        factors[i] = (2*i - 1) * p
    return(factors)


'''
    Computing the NLFT under the Coalescent
    @param n - number of current samples in the present generation
    @param t - number of generations in the Moran model to run until
'''
def computeNLFTCoalescent(n, t, N, factors=None):
    if factors is None:
        factors = precompute(n)
    N0 = N[0]
    # iterating through the Moran generations
    exponent = 0.
    for i in range(1,t+1):
        expectedValue = 0.
        exponent += (2*(i - i-1)) / (float(N[i])**2)

        for j in range(0,n+1):
            expectedValue += np.exp(-j*(j-1)/2 * exponent) * factors[j]
        print(expectedValue)


'''
    Computing some of the quantities from Polanski and Kimmel
        (TODO)
'''


def computeV():
    pass


def computeW():
    pass

















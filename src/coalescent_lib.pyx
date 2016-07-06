
'''
    Computing Genealogical Properties under the Coalescent
'''

from libc.math cimport exp


# TODO : set up some sort of epoch class here that we can setup files for 
    # - this way we can actually test piecewise exponential models in coalescent time

'''
    Function to precompute some values for the sums
    NOTE : factors are only for the expectation (but can be done for the variance as well)
'''
cdef precompute(int n):
    factors = [0.0] * (n+1)
    cdef double p = 1.0
    for i in range(1, n+1):
        p *= 1.0 * (n - i + 1) / (n + i - 1)
        factors[i] = (2*i - 1) * p
    return(factors)

'''
    Computing the Expected NLFT under the Coalescent (e.g. Tavare)
    @param n - number of current samples in the present generation
    @param t - number of generations in the Moran model to run until
    @param N - population size history (in Moran generations)
'''
def computeNLFTCoalescent(n, t, N, factors=None):
    if factors is None:
        factors = precompute(n)
    # iterating through the Moran generations
    cdef double omega = 0.
    cdef double expectedValue = 0.
    cdef int i,j
    print("Gen\tNLFT")
    for i in range(1,t+1):
        expectedValue = 0.0
        omega += 2. / (float(N[i])**2)
        for j in range(1,n+1):
            expectedValue += exp(-1. * j * (j-1.) / 2. * omega) * factors[j]
        print("%d\t%f" % (i,expectedValue))
        # print(i, expectedValue, sep="\t")

# Equation 12 from Polanski and Kimmel (Genetics 2003)
cdef computeV(int n):
    v = [0] * (n+1)
    v[2] = (n-1.) / (n+1.)
    for j in range(4, n+1, 2):
        v[j] = v[j-2] * (n - j + 2) / (n + j - 2) * (n- j + 1) / (n + j - 1)
    for j in range(2, n+1, 2):
        v[j] *= 2. * (2. * j - 1.)
    return(v)


# Equation 13-15 from Polanski and Kimmel (Genetics 2003)
cdef computeW(int n, int b):
    w = [0] * (n+1)
    w[2] = 6. / (n + 1.)
    w[3] = 30. / (n + 1.) * (n - 2.*b) / (n + 2.)
    for j in range(2, n-2+1):
        coef1 = - (1. + j) / j * (3. + 2.*j) / (2.*j - 1)  * (n - j) / (n + j + 1.)
        coef2 = (3. + 2.*j) * (n - 2.*b) / j / (n + j + 1.)
        w[j+2] = coef1 * w[j] + coef2 * w[j+1]
    return(w)

# Equation 3 from Polanski and Kimmel (Genetics 2003)
# TODO : note right now it is just handling constant popsize in a Moran scaling...
cdef computeEj(int n, N):
    Ej = [0.] * (n+1)
    for j in range(2,n+1):
        jchoose2 = j*(j-1)/2
        # Note : this is just the constant case for now!
        t = len(N)
        omega = 2.0 / (float(N[0])**2) * t
        Ej[j] = (float(N[0])**2) / (j*(j-1)) * exp(-jchoose2 * omega)
    return(Ej)


# Computes the first maxA entries of the normalized SFS for a sample of size n 
# Eq (8) in Polanski and Kimmel (Genetics 2003)
def computeSFSHelper(n, maxA, N):
    # precomputing some stuff
    Ej = computeEj(n, N)
    V = computeV(n)
    den = sum([Ej[j] * V[j] for j in range(2,n+1)])
    num = [0.] * maxA
    for b in range(1, min(maxA, n-1)):
        W = computeW(n, b)
        for j in range(2,n+1):
            num[b] += Ej[j] * W[j]
    return({'sfs':num , 'norm':den})

def computeSFSNormalized(n, maxA, N):
    sfs = computeSFSHelper(n, maxA, N)
    sfs_norm = [sfs['sfs'][i] / sfs['norm'] for i in range(maxA)]
    return(sfs_norm)

def computeSFSUnNormalized(n, maxA, N):
    sfs = computeSFSHelper(n, maxA, N)
    return(sfs['sfs'])


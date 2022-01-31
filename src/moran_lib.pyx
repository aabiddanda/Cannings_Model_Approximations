
'''
    Library for computing geneological quantities under the Moran Model
'''

import numpy as np

'''
    Function to compute probability of m ancestors in Moran Model
    @param n - number of current samples
    @param m - number of ancestors
    @param N - population size
'''
cdef double prob_lineages(int n, int m, int N):
    if (m < (n-1)) | (m > n) :
        return(0.0)
    else:
        n1 = <double> n
        N1 = <double> N
        prob = (n1 * (n1-1.0)) / (N1**2.0)
        if m == (n-1):
            return(prob)
        if m == n:
            return(1-prob)

'''
    Function to compute probability of m descendents after t Moran generations
    @param n - current sample size
    @param t - duration (in Moran generations)
    @param N - constant population size for duration
    @param acc (optional) - previous probabilities
'''
def prob_lineages_step(int n, int t, int N, acc=None):
    if acc is None:
        acc = [0.] * (n+1)
        acc[n] = 1.
    if len(acc) != n+1:
        raise ValueError('Dimension mismatch in probability vector!')
    cdef int i,j
    for i in range(t):
        new_acc = [0.] * (n+1)
        for j in range(n+1):
            if j == n:
                new_acc[j] = acc[j] * prob_lineages(j, j, N)
            else:
                new_acc[j] = prob_lineages(j, j, N) * acc[j] + prob_lineages(j+1, j, N) * acc[j+1]
        acc = new_acc
    return(acc)

def nlft_moran(int n, int t, int delta, int N):
    if t % delta != 0:
        raise ValueError('Delta does not divide time evenly')
    curProb = [0.0] * (n+1)
    curProb[n] = 1.0
    timeSlice = range(delta, t+1, delta)
    print("Gen\tE_NLFT\tVAR_NLFT")
    for x in timeSlice:
        current_probs = prob_lineages_step(n, delta, N, acc = curProb)
        curProb = current_probs
        E_NLFT = sum([i*curProb[i] for i in range(n+1)])
        E_NLFT2 = sum([(i**2.)*curProb[i] for i in range(n+1)])
        var_NLFT = E_NLFT2 - (E_NLFT**2.)
        print("%d\t%0.8f\t%0.8f" % (x, E_NLFT, var_NLFT))

'''
    Calculating gamma (branch lengths)
    @param N - population size
    @param a - subtending branch
    @param b - other fraction in sample
'''
def gamma_constant(int N, int a, int b):
    if a == 1 & b == 1:
        return(N**2. / 2)
    if a == 1:
        pass



'''
    Reads a Moran Model from a demography specifying file
'''
def readMoranModel():
    pass

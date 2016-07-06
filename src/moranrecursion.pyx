
'''
    Module for recursion computations under the Moran model
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
    @param N - vector of population sizes per generation
    @param acc (optional) - previous probabilities 
'''
def prob_lineages_step(int n, int t, N, acc=None):
    if acc is None:
        acc = [0 for i in range(0,n+1)]
        acc[n] = 1
    if len(acc) != n+1:
        raise ValueError('Dimension mismatch in probability vector')
    for i in range(t):
        new_acc = [0 for x in range(0,n+1)]
        for j in range(n+1):
            if j == n:
                new_acc[j] = acc[j] * prob_lineages(j, j, N[i+1])
            else:
                new_acc[j] = prob_lineages(j, j, N[i+1]) * acc[j] + prob_lineages(j+1, j, N[i+1]) * acc[j+1]
        acc = new_acc
    return(acc)

# TODO : write a matrix to compute transition densities Q[n,m]^(t) for a better arbitrary computation


def nlft_moran(int n, int t, delta, N):
    if t % delta != 0:
        raise ValueError('Delta does not divide time evenly')
    probMat = np.zeros([t/delta, n+1], dtype=float)
    probMat[0,n] = 1.0
    cdef int curRow = 0
    timeSlice = range(delta, t, delta)
    l = len(N)
    for x in timeSlice:
        print(curRow)
        current_probs = prob_lineages_step(n, delta, N[x:l], acc = probMat[curRow, ])
        curRow += 1
        probMat[curRow, ] = current_probs
    return(probMat)



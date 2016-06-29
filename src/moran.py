'''
    Module of functions for computations under the Moran Model
'''

import numpy as np
import scipy as sp


'''
    Function to compute the probabiity of n current lineages
        having m ancestors a generation ago
    @param n - current number of lineages
    @param m - number of parental lineages
    @param t - current time step
    @param N - vector of population sizes 
'''
def prob_lineages(n, m, N):
    # TODO : check that m < n 
    if m < (n-1) : 
        return(0.0)
    else:
        prob = n*(n-1.0)/(N**2)
        if (m == n-1):
            return(prob)
        if (m == n):
            return(1-prob)

'''
    Function to compute the probability of m lineages from n samples 
        t generations ago
    @param n - current sample size
    @param t - time step (in Moran Generations)
    @param N - vector of population sizes through time
    @param acc - vector of probabilities 
'''
def prob_lineages_step(n, t, N , acc=None):
    if acc is None:
        acc = [0 for i in range(0,n+1)]
        acc[n] = 1
    if len(acc) != (n+1):
       raise ValueError('dimension mismatch in probability vector') 
    for i in range(0,t):
        new_acc = [0 for x in range(0,n+1)]
        for j in range(0, n+1):
            if j == n:
                new_acc[j] = acc[j] * prob_lineages(j, j, N[i+1])
            else:
                new_acc[j] = prob_lineages(j, j, N[i+1]) * acc[j] + prob_lineages(j+1, j, N[i+1]) * acc[j+1]
        acc = new_acc
    return(acc)


'''
    Function to compute the expected number of lineages as a function of time
    @param n - current sample size
    @param t - time duration 
    @param delta - time increments (unclear what this should be)
    @param N - population sizes
    @return probMat - numpy matrix providing probabilities of lineages at each time-increment
'''
def nlft_moran(n, t, delta,  N):
    if t % delta != 0:
        raise ValueError('Delta does not divide time evenly!')
    probMat = np.zeros([t/delta, n+1], dtype=float)
    probMat[0,n] = 1.0
    curRow = 0
    timeSlice = range(delta,t, delta)
    l = len(N)
    for x in timeSlice:
        current_probs = prob_lineages_step(n, delta, N[x:l], acc = probMat[curRow,])
        curRow += 1
        probMat[curRow, ] = current_probs
    return(probMat)


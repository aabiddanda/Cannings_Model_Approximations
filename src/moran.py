
'''
    Module of functions for computations under the Moran Model
'''

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# TODO : find some libraries for numerical analysis if needed

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


# TODO : make these functions much faster
# TODO : plug in some cython in here if needed
def prob_lineages_step(n, t, N):
    acc = [0 for i in range(0,n+1)]
    acc[n] = 1
    for i in range(0,t):
        new_acc = [0 for x in range(0,n+1)]
        for j in range(0, n+1):
            if j == n:
                new_acc[j] = acc[j] * prob_lineages(j,j,N[i+1])
            else:
                new_acc[j] = prob_lineages(j,j,N[i+1])*acc[j] + prob_lineages(j+1, j, N[i+1])*acc[j+1]
        acc = new_acc
    return(acc)


'''
    Function to compute the expected number of lineages as a function of time
    @param n - current population size
    @param t - time duration 
    @param delta - time increments
    @param N - population sizes
'''
def nlft_moran(n, t, delta,  N):
    expM = [0 for i in range(0,t, delta)]
    current_prob = [0 for i in range(0,n+1)]
    current_prob[n] = 1
    l = len(N)
    for x in range(0,t, delta):
        # TODO : should do some kind of recursion here as well..
        revised_probs = prob_lineages_step(n, delta, Ne[x:l])











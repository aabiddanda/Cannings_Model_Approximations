#!/usr/local/bin/python3


import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

''' 
	Probability that n individuals at generation t have m 
		distinct ancestors at time t+1
	@param n : number of current lineages in generation (t)
	@param m : number of parents in generation (t+1)
	@param N_t1 : population size at generation (t+1)
'''
def prob_anc(n, m, N_t1):
	acc = [0 for i in range(0,m)]
	acc[0] = 1
	for i in range(1,n):
		new_acc = [0 for i in range(0,m)]
		for j in range(1,m):
			new_acc[j] = (N_t1 - j + 1)/N_t1 * acc[j-1] + (j/N_t1)*acc[j]
		acc = new_acc
	return(acc[m-1])

# Just to visualize this further...
def prob_anc_hist(n, m_list, N):
	probs = [prob_anc(n,i,N) for i in m_list]
	plt.bar(m_list, probs)
	plt.ylabel('Probability')
	plt.xlabel('m')
	plt.show()




''' 
	Probability that n individuals at generation t have m 
		distinct ancestors at time t+1
	@param n : number of current lineages in generation (t)
	@param N_t1 : population size at generation (t+1)
'''
# TODO : revise this as it may be incorrect (off by one)
def prob_anc(int n, int N_t1):
    acc = [0.0] * (n+1)
    acc[0] = 1.
    for i in range(1,n):
        new_acc = [0.0] * (n+1)
        for j in range(1,n):
            new_acc[j] = (N_t1 - j + 1) / N_t1 * acc[j-1] + (j/N_t1)*acc[j]
        acc = new_acc
    return(acc)


'''
    Compute the number of lineages as a function of time

'''
def nlft_dtwf(int n, int t):
    pass



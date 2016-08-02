
''' 
	Probability that n individuals at generation t have m 
		distinct ancestors at time t+1
	@param n : number of current lineages in generation (t)
	@param N_t1 : population size at generation (t+1)
'''
def prob_anc(int n, int N_t1):
    acc = [0.0] * (n+1)
    acc[0] = 1.
    cdef int i = 1
    for i in range(1,n+1):
        new_acc = [0.0] * (n+1)
        for m in range(1,n+1):
            new_acc[m] = (N_t1 - m + 1) / N_t1 * acc[m-1] + (m / N_t1) * acc[m]
        acc = new_acc
    return(acc)

'''
    Calculating the original transition matrices
    @param n - sample size
    @param N_t1 - population size a generation ahead
'''
def prob_mat(int n, int N_t1):
    assert n <= N_t1
    Q = [[0.0]*(n+1) for x in range(n+1)]
    Q[0][0] = 1.0
    cdef int i = 1
    cdef int j
    while i <= n:
        j = 1
        while j <= i:
            Q[i][j] = Q[i-1][j-1]*(N_t1 - j + 1.0) / N_t1 + Q[i-1][j]*j / N_t1
            j += 1
        i += 1 
    return(Q)

'''
    @param n - current sample size
    @param N_t1 - population size a gen in the past
    @param eps - threshold on probabilities
'''
def prob_mat_trunc(int n, int N_t1, double eps):
    pass


# TODO : develop this a little bit more
'''
    Compute the number of lineages as a function of time
    @param n - original number of lineages
    @param t - number of DTWF generations to run until
    @param N - currently only handles constant popsize 
'''
# TODO : make the popsize a vector
def nlft_dtwf(int n, int N, int t):
   prob = [0.0] * (n+1)
   prob[n] = 1.0
   cdef int t1, m, k
   mat = prob_mat(n,N)
   print("T\tE_NLFT")
   t1 = 1
   while t1 <= t:
       new_prob = [0.0] * (n+1)
       for m in range(1, n+1):
           for k in range(m, n+1):
               new_prob[m] += mat[k][m] * prob[k]
       prob = new_prob
       E_NLFT = sum([i*prob[i] for i in range(1,n+1)])
       print("%d\t%0.8f" % (t1,E_NLFT))
       t1 += 1





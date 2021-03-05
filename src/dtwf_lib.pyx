
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



'''
    Calculating the branch length that subtends individuals:
    @param maxA - maximum A entry that we want to calculate branch lengths for
    @param n - the current sample size
    @param N - the current (constant) population size
    @param Q - lineage transition matrix
'''
# TODO : should define a truncated version 
def calc_gamma_const(int maxA, int n,  int N, Q):
    gamma_const = [[0.0]*(n+1) for i in range(min(maxA,N)+1)]
    cdef int a,b
    cdef double f, ans
    #gamma_const[1][1] = N
    for a in range(1, min(maxA,N) + 1):
        for b in range(1, n+1):
            if (a + b <= n) & (a+b <= N):
                if (a == 1):
                    #print(b)
                    f = 1.0 - Q[b+1][b+1]
                    ans = 1.0 / f
                    for m in range(1, b):
                        ans += (N-m) / N * Q[b][m] / f * gamma_const[a][m]
                    gamma_const[a][b] = ans
                else:
                    ans = 0.0
                    for j in range(1,a+1):
                        f = 1.0
                        for i in range(j):
                            f *= 1. * (N - b - i) / (N - i)
                        for k in range(1,b+1):
                            if (j != a) | (k != b):
                                ans += Q[a][j]*Q[b][k] * f / (1 - Q[a+b][a+b]) * gamma_const[j][k]
                                f *= 1. * (N - j - k) / (N - k)
                    gamma_const[a][b] = ans
    return(gamma_const)








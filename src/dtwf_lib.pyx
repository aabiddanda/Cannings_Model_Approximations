
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
    for i in range(1,n+1):
        new_acc = [0.0] * (n+1)
        for m in range(1,n+1):
            new_acc[m] = (N_t1 - m + 1) / N_t1 * acc[m-1] + (m / N_t1) * acc[m]
        acc = new_acc
    return(acc)


'''
    Calculating the whole transition matrix
'''
def prob_mat(int n, int N_t1):
    mat = [[0.0 for i in range(n+1)]]
    cdef int k = 1
    for k in range(1, n+1):
        cur_row = prob_anc(k, N_t1)
        cur_row.extend([0.0 for i in range(1,n+1-k)])
        mat.append(cur_row)
    return(mat)

'''
    Compute the number of lineages as a function of time
    @param n - original number of lineages
    @param t - number of DTWF generations to run until
    @param N - currently only handles constant popsize 
'''
def nlft_dtwf(int n, int N, int t):
   prob = [0.0] * (n+1)
   prob[n] = 1.0
   cdef int t1 = 1
   print("T\tE_NLFT")
   for t1 in range(1,t+1):
       new_prob = [0.0] * (n+1)
       mat = prob_mat(n, N)
       for m in range(1, n+1):
           for k in range(m, n+1):
               new_prob[m] += mat[k][m] * prob[k]
       prob=new_prob
       E_NLFT = sum([i*prob[i] for i in range(1,n+1)])
       print("%d\t%0.8f" % (t1,E_NLFT))


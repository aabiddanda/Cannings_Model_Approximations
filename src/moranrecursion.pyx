


# Defines a simple function
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


def dummy(int n, int m, int N):
    return(prob_lineages(n,m,N))


# TODO : make more general functions in here too
def prob_lineages_step(int n, int t, N, acc=None):
    if acc is None:
        acc = [0 for i in range(0,n+1)]
        acc[n] = 1
    if len(acc) != n+1:
        raise ValueError('dimension mismatch in probability vector')
    for i in range(t):
        new_acc = [0 for x in range(0,n+1)]
        for j in range(n+1):
            if j == n:
                new_acc[j] = acc[j] * prob_lineages(j, j, N[i+1])
            else:
                new_acc[j] = prob_lineages(j, j, N[i+1]) * acc[j] + prob_lineages(j+1, j, N[i+1]) * acc[j+1]
        acc = new_acc
    return(acc)



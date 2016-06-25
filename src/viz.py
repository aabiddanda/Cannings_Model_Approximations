
import moran as mp
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


'''
    Plotting Function to make first figure
    @param n - current number of lineages
    @param t - number of Moran generations that have passed
    @param N - vector of population sizes across generations
'''
def plot_figure1(n,t,N):
    y = mp.prob_lineages_step(n,t,N)
    l = len(y)
    y = y[1:l]
    x = [i for i in range(1,len(y)+1)]
    plt.bar(x, y, linewidth=0)
    plt.ylabel(r'\textit{Probability}')
    plt.xlabel(r'\textit{m}')
    plt.savefig("../plots/figure1.eps", dpi=1000)



#!/usr/local/bin/python3

import moran as mp
import matplotlib.pyplot as plt
import argparse as arg

# Setting Matplotlib preferences
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


'''
    Plotting Function to make first figure
    @param n - current number of lineages
    @param t - number of Moran generations that have passed
    @param N - vector of population sizes across generations
    @param outfile - outfile parameter to write image to
    @param xlim (optional) - xlimits of plot
'''
def plot_figure1(n, t, N, outfile, xlim=None):
    y = mp.prob_lineages_step(n,t,N)
    l = len(y)
    y = y[1:l]
    x = [i for i in range(1,len(y)+1)]
    plt.bar(x, y, linewidth=0, align='center')
    plt.ylabel(r'\textbf{Probability}')
    plt.xlabel(r'\textit{m}')
    if xlim is not None:
        plt.xlim(xlim)
    # TODO : should define parameter for creating an output file here
    plt.savefig(outfile, dpi=1000)


def plot_figure2(n,t,delta, N):
    pass



if __name__ == '__main__':
    # Parse all arguments
    parser = arg.ArgumentParser()
    parser.add_argument('-o', '--outfile', required=True, help='output figure file')
    parser.add_argument('-figure1', action='store_true', required=False, help='Creating Figure 1')
    args = parser.parse_args()

    # Going through all of the cases 
    if args.figure1:
        Ne = [20000 for i in range(0, int(1e6))]
        plot_figure1(250, 20000, Ne, args.outfile, xlim=[236,251])





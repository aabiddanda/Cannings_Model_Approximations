#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import argparse as arg

import moranrecursion as mp
import dtwf


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


'''
    Function to compute the densities of lineages lost in one generation under both the Moran and DTWF model
'''
def plot_figure2(n,t, N, outfile, xlim=None):
   ymoran = mp.prob_lineages_step(n,t,N)
   m_list = [i for i in range(1,n+1)]
   ydtwf = [dtwf.prob_anc(n,i,N[0]) for i in m_list]
   l = len(ymoran)
   ymoran = ymoran[1:l]
   x = [i for i in range(1,n+1)]
   f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
   ax1.bar(x,ymoran, linewidth=0, align='center')
   ax2.bar(x,ydtwf, linewidth=0, align='center')
   ax1.set_title('Moran Model')
   ax2.set_title('DTWF')
   plt.ylabel(r'\textbf{Probability}')
   ax1.set_xlabel(r'\textit{m}')
   ax2.set_xlabel(r'\textit{m}')
   if xlim is not None:
       ax1.set_xlim(xlim)
       ax2.set_xlim(xlim)
   plt.savefig(outfile, dpi=1000)

if __name__ == '__main__':
    # Parse all arguments
    parser = arg.ArgumentParser()
    parser.add_argument('-o', '--outfile', required=True, help='output figure file')
    parser.add_argument('-figure1', action='store_true', required=False, help='Creating Figure 1')
    parser.add_argument('-figure2', action='store_true', required=False, help='Creating Figure 2')
    args = parser.parse_args()

    # Going through all of the cases 
    if args.figure1:
        Ne = [20000 for i in range(int(1e6))]
        plot_figure1(250, 20000, Ne, args.outfile, xlim=[236,251])
    
    if args.figure2:
        Ne = [20000 for i in range(int(1e6))]
        plot_figure2(250, 20000, Ne, args.outfile, xlim=[236,251])



import matplotlib.pyplot as plt
import argparse as arg

import moran_lib as mp
import dtwf_lib as dtwf


# Setting Matplotlib preferences
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('figure', autolayout=True)

'''
    Function to compute the densities of lineages lost in one generation under both the Moran and DTWF model
'''
def plot_figure1(n,t, N, outfile, xlim=None):
   ymoran = mp.prob_lineages_step(n,t,N)
   ydtwf = dtwf.prob_anc(n,N[0])
   l = len(ymoran)
   print(sum(ymoran))
   print(sum(ydtwf))

   print(l, len(ydtwf))
   ymoran = ymoran[1:l]
   ydtwf = ydtwf[1:l]
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


'''
    Comparing coalescent predictions to discrete Moran Model 
    @param filenames - filenames for comparisons
'''
def plot_figure2(outfile):
    coal_exp = []
    moran_exp = []
    with open('../data/coalescent_nlft2000.txt') as f:
        next(f)
        for line in f:
            e_nlft_coal = float(line.split()[1])
            coal_exp.append(e_nlft_coal)
    with open('../data/moran_nlft2000.txt') as f:
        next(f)
        for line in f:
            e_nlft_moran = float(line.split()[1])
            moran_exp.append(e_nlft_moran)
    coal_exp = coal_exp[0:(len(coal_exp)-1)]
    # print(len(coal_exp))
    # print(len(moran_exp))
    t = [i for i in range(1,len(coal_exp)+1)]
    error = [(moran_exp[i] - coal_exp[i]) / coal_exp[i] * 100.0 for i in range(0,len(coal_exp))]
    plt.plot(t, error)
    coal_exp200 = []
    moran_exp200 = []
    with open('../data/coalescent_nlft200.txt') as f:
        next(f)
        for line in f:
            e_nlft_coal = float(line.split()[1])
            coal_exp200.append(e_nlft_coal)
    with open('../data/moran_nlft200.txt') as f:
        next(f)
        for line in f:
            e_nlft_moran = float(line.split()[1])
            moran_exp200.append(e_nlft_moran)
    coal_exp200 = coal_exp200[0:(len(coal_exp200)-1)]
    error200 = [(moran_exp200[i] - coal_exp200[i]) / coal_exp200[i] * 100.0 for i in range(0,len(coal_exp200))]
    plt.plot(t, error200)
    plt.legend(['n = 2000', 'n = 200'], loc='upper right')
    plt.xlabel(r'\textit{t}')
    plt.ylabel(r'$\frac{E(A_n^M(t)) - E(A_n^C(t))}{E(A_n^C(t))} \times 100\%$')
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
        Ne = [200 for i in range(int(1e6))]
        plot_figure1(20, 200/2, Ne, args.outfile)
    if args.figure2:
        plot_figure2(args.outfile)
    


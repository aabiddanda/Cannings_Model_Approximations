
import matplotlib.pyplot as plt
import argparse as arg

import moran_lib as mp
import dtwf_lib as dtwf


# Setting Matplotlib preferences
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('figure', autolayout=True)

'''
    Function to compute the densities of lineages lost in 
        one generation under both the Moran and DTWF model
'''
# TODO : should adaptively set the xlim if possible
def plot_figure1(n, t, N, outfile, xlim=None):
   ymoran = mp.prob_lineages_step(n,t,N)
   ydtwf = dtwf.prob_anc(n,N[0])
   l = len(ymoran)
   ymoran = ymoran[1:l]
   ydtwf = ydtwf[1:l]
   x = [i for i in range(1,n+1)]
   # Computing Expectations
   nl_moran = sum([i*ymoran[i] for i in range(n)])
   nl_dtwf = sum([i*ydtwf[i] for i in range(n)])
   print("E(NLFT | Moran) = %0.8f\nE(NLFT | DTWF) = %0.8f" % (nl_moran, nl_dtwf))
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
    Helper function to read from NLFT output files
'''
def read_nlft(filelist):
    l = len(filelist)
    E_NLFT = []
    for i in range(0, l):
        cur_nlft = []
        with open(filelist[i]) as f:
            next(f)
            for line in f:
                e_nlft = float(line.split()[1])
                cur_nlft.append(e_nlft)
        E_NLFT.append(cur_nlft)
    return(E_NLFT)

'''
    Comparing coalescent predictions to discrete Moran Model 
    @param outfile - actual output eps file
    @param moranfiles - nlft output from moran.py
    @param coalfiles - nlft output from coalescent.py
    @param legend - labels to give legend (i.e. sample sizes)
'''
def plot_figure2(outfile, moranfiles, coalfiles, legend):
    assert len(moranfiles) == len(coalfiles)
    coal_exp = read_nlft(coalfiles)
    moran_exp = read_nlft(moranfiles)
    t = [i for i in range(1, len(coal_exp[0]) + 1)]
    for l in range(len(coal_exp)):
        cur_coal_exp = coal_exp[l]
        cur_moran_exp = moran_exp[l]
        cur_error = [(cur_moran_exp[i] - cur_coal_exp[i]) / cur_coal_exp[i] * 100.0 for i in range(len(cur_coal_exp))]
        plt.plot(t, cur_error)
    plt.legend(legend, loc='lower right')
    plt.xlabel(r'\textit{t}')
    plt.ylabel(r'$\frac{E(A_n^M(t)) - E(A_n^C(t))}{E(A_n^C(t))} \times 100\%$')
    plt.savefig(outfile, dpi=1000)


if __name__ == '__main__':
    # Parse all arguments
    parser = arg.ArgumentParser()
    parser.add_argument('-o', '--outfile', required=True, help='output figure file')
    parser.add_argument('-n', type=int, required=False, help='sample size', default=250)
    parser.add_argument('-N', type=int, required=False, help='constant population size', default=20000)
    parser.add_argument('-figure1', action='store_true', required=False, help='Creating Figure 1')
    parser.add_argument('-figure2', action='store_true', required=False, help='Creating Figure 2')
    parser.add_argument('-moranfiles', type=str, nargs='+', required=False, help='files detailing Moran NLFT')
    parser.add_argument('-coalfiles', type=str, nargs='+', required=False, help='files detailing Coalescent NLFT')
    parser.add_argument('-legend2', type=str, nargs='+', required=False, help='legend labels for figure2')
    args = parser.parse_args()

    # Going through all of the cases 
    if args.figure1:
        Ne = [args.N for i in range(int(1e6))]
        min_x = 0 if args.n - 30 < 0 else args.n - 30
        plot_figure1(args.n, args.N/2, Ne, args.outfile, xlim=[min_x, args.n+3])
    if args.figure2:
        print(args.moranfiles)
        print(args.coalfiles)
        plot_figure2(args.outfile, args.moranfiles, args.coalfiles, args.legend2)

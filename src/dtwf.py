'''
    Wrapper file for DTWF computations.

'''

import argparse as arg
import dtwf_lib as dtwf

def prob_lineages_dtwf(n, N_t1):
    return(dtwf.prob_anc(n, N_t1))

def nlft_dtwf(n, N, t):
    dtwf.nlft_dtwf(n,N,t)

if __name__ =='__main__':
    # Parse all arguments given
    parser = arg.ArgumentParser()
    parser.add_argument('-n', '--sampsize', type=int, required=True, help='sample size argument')
    parser.add_argument('-N', '--popsize', type=int, required=False, help='constant population size')
    parser.add_argument('-t', type=int, required=False, help='time length')
    parser.add_argument('-prob', '--prob' , action='store_true', required=False)
    parser.add_argument('-nlft', action='store_true', required=False)
    args = parser.parse_args()
    
    # Do something in here
    if args.prob : 
        print(prob_lineages_dtwf(args.sampsize, args.popsize))
    if args.nlft:
        nlft_dtwf(args.sampsize, args.popsize, args.t)


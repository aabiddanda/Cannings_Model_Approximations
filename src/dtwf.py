'''
    Wrapper file for DTWF computations.

'''

import argparse as arg
import dtwf_lib as dtwf
import numpy as np 

if __name__ =='__main__':
    # Parse all arguments given
    parser = arg.ArgumentParser()
    parser.add_argument('-n', type=int, required=True, help='sample size argument')
    parser.add_argument('-N', type=int, required=False, help='constant population size')
    parser.add_argument('-t', type=int, required=False, help='time length')
    parser.add_argument('-e', type=float, required=False, help='error parameter')
    parser.add_argument('-prob', '--prob' , action='store_true', required=False)
    parser.add_argument('-nlft', action='store_true', required=False)
    args = parser.parse_args()
    
    # Do something in here
    if args.prob :
        mat = dtwf.prob_mat(args.n, args.N)
        print(np.array(mat))
    if args.nlft:
        dtwf.nlft_dtwf(args.n, args.N, args.t)


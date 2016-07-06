
'''
    Computing Genealogical Properties under the Coalescent
'''

import argparse as arg
import coalescent_lib as coal

if __name__ == '__main__':
    parser = arg.ArgumentParser()
    parser.add_argument('-n', '--sampsize', required=True, type=int, help='initial sample size')
    parser.add_argument('-A', required=False, type=int, help='number of entries in hte SFS to calculate')
    parser.add_argument('-t', required=False, type=int, help='Time steps to evaluate')
    parser.add_argument('-nlft', action='store_true', required=False, help='Compute NLFT quantities')
    parser.add_argument('-sfs', action='store_true', required=False, help='Compute the expected SFS')
    parser.add_argument('-norm', action='store_true', required=False, help='Normalized vs. Un-Normalized SFS')
    args = parser.parse_args()
  

    # Outputing the SFS or the NLFT based on a number of arguments 
    if args.sfs:
        N = [20000 for i in range(0,200000)]
        if args.norm:
            sfs_norm = coal.computeSFSNormalized(args.sampsize,  args.A, N)
            print(sfs_norm)
            print(sum(sfs_norm))
        else:
            sfs = coal.computeSFSUnNormalized(args.sampsize, args.A, N)
            print(sfs)
    if args.nlft:
        N = [20000] * (args.t + 1)  
        coal.computeNLFTCoalescent(args.sampsize, args.t, N)



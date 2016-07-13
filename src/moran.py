'''
    File to compute Geneological quantities under the Moran Model
'''

import argparse as arg
import moran_lib as mp 

if __name__ == '__main__':
    parser = arg.ArgumentParser()
    parser.add_argument('-n', '--sampsize', required=True, type=int, help='initial sample size (haploid)')
    parser.add_argument('-N', required=False, type=int, default=20000, help='population size')
    parser.add_argument('-t', required=False, type=int, help='number of Moran generations to run for')
    parser.add_argument('-nlft', required=False, action='store_true', help='compute NLFT as a function of time under the Moran Model')
    args = parser.parse_args()

    if args.nlft:
        # N = [args.N] * (args.t + 2)
        mp.nlft_moran(args.sampsize, args.t, 1, args.N)

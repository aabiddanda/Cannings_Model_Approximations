'''
    File to compute Geneological quantities under the Moran Model
'''

import argparse as arg
import moran_lib as mp 

if __name__ == '__main__':
    parser = arg.ArgumentParser()
    parser.add_argument('-n', required=True, type=int, help='initial sample size (haploid)')
    parser.add_argument('-nlft', required=False, action='store_true', help='compute NLFT as a function of time under the Moran Model')
    args = parser.parse_args()

    if args.nlft:
        print('Coming Soon!')

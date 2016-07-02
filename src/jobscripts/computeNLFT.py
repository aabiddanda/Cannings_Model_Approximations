
'''
    Script to compute the NLFT under the Moran Model
'''

import argparse as arg
import numpy as np 
import moranrecursion as mp 


# Some functions...
def computeNLFTMoran(n, t, delta, Ne):
    pass

if __name__ =='__main__':
    # Parse all arguments given
    parser = arg.ArgumentParser()
    parser.add_argument('-n', '--n', required=True, help='sample size')
    parser.add_argument('-t', '--t', required=True, help='Time Steps')
    parser.add_argument('-delta', '--delta', required=True, help='Change in timesteps.')
    args = parser.parse_args()

    
        


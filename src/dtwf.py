"""Script to print statistics under the DTWF."""
import argparse as arg

import dtwf_lib as dtwf
import numpy as np

if __name__ == "__main__":
    parser = arg.ArgumentParser()
    parser.add_argument("-n", type=int, required=True, help="sample size")
    parser.add_argument("-N", type=int, required=False, help="population size")
    parser.add_argument("-t", type=int, required=False, help="time length")
    parser.add_argument("-e", type=float, required=False, help="error")
    parser.add_argument("-prob", "--prob", action="store_true", required=False)
    parser.add_argument("-nlft", "--nlft", action="store_true", required=False)
    args = parser.parse_args()

    if args.prob:
        mat = dtwf.prob_mat(args.n, args.N)
        print(np.array(mat))
    if args.nlft:
        dtwf.nlft_dtwf(args.n, args.N, args.t)

"""Script for computing geneological quantities under the Moran Model."""

import argparse as arg

import moran_lib as mp

if __name__ == "__main__":
    parser = arg.ArgumentParser()
    parser.add_argument(
        "-n",
        "--sampsize",
        required=True,
        type=int,
        help="initial sample size (haploid)",
    )
    parser.add_argument(
        "-N", required=False, type=int, default=20000, help="population size"
    )
    parser.add_argument(
        "-t", required=False, type=int, help="Number of Moran generations"
    )
    parser.add_argument(
        "-nlft",
        required=False,
        action="store_true",
        help="Compute NLFT as a function of time under the Moran Model",
    )
    args = parser.parse_args()

    if args.nlft:
        mp.nlft_moran(args.sampsize, args.t, 1, args.N)

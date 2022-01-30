"""Utility functions for genealogical quantities."""


def readDTWF(dtwffile):
    """Read and print out population sizes from a DTWF file."""
    popsizes = []
    gens = []
    final_size = 0
    with open(dtwffile, "r") as f:
        next(f)
        final_size = f.readline()
        final_size = int(final_size)
        for line in f:
            lnsplt = line.split()
            time_length = int(lnsplt[0])
            gens.append(time_length)
            popsizes.append(int(lnsplt[1]))
    return popsizes

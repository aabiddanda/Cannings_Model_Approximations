'''
    General Utility functions for genealogical quantities
'''


# Create an epoch class that should help out
def readDTWF(dtwffile):
    popsizes = []
    gens = []
    final_size = 0
    with open(dtwffile, 'r') as f:
        next(f)
        final_size = f.readline()
        final_size = int(final_size)
        for line in f:
            lnsplt = line.split()
            time_length = int(lnsplt[0])
            gens.append(time_length)
            popsizes.append(int(lnsplt[1]))
    print(final_size)
    print(gens)
    print(popsizes)
    return(popsizes)


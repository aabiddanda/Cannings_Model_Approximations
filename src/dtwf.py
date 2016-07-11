
'''
This is a standard template for a python
	script with arguments
'''

import argparse as arg
import dtwf_lib as dtwf

# Some functions...
def foo():
    pass


if __name__ =='__main__':
	# Parse all arguments given
	parser = arg.ArgumentParser()
        parser.add_argument('-n', '--sampsize', type=int, required=True, help='sample size argument')
	args = parser.parse_args()

	# TODO : do something here
        

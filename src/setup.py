
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from subprocess import call
import numpy

system = 'Mac'

# Defining the different libraries to set up 
extensions = [
        Extension('moran_lib', 
            ['moran_lib.pyx'],
            extra_compile_args=['-w']
            ),
        Extension('coalescent_lib',
            ['coalescent_lib.pyx'],
            extra_compile_args=['-w']),
        Extension('dtwf_lib', 
            ['dtwf_lib.pyx'],
            extra_compile_args=['-w'])
        ]
setup(ext_modules = cythonize(extensions))

# Linking the Mac Module to 
if system == 'Mac':
    call(['mv', 'moran_lib.cpython-35m-darwin.so', 'moran_lib.so'])
    call(['mv', 'coalescent_lib.cpython-35m-darwin.so', 'coalescent_lib.so'])
    call(['mv', 'dtwf_lib.cpython-35m-darwin.so', 'dtwf_lib.so'])

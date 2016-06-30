
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from subprocess import call

system = 'Mac'

extensions = [Extension("moranrecursion", ["moranrecursion.pyx"])]

setup(ext_modules = cythonize(extensions))

# Linking the Mac Module to 

if system == 'Mac':
    call(['mv', 'moranrecursion.cpython-35m-darwin.so', 'moranrecursion.so'])


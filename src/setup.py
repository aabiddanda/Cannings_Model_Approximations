"""Setup script for Cython Modules (currently only Mac)."""
from distutils.core import setup
from distutils.extension import Extension
from subprocess import call

from Cython.Build import cythonize

system = "Mac"

# Defining the different libraries to set up
extensions = [
    Extension("moran_lib", ["moran_lib.pyx"], extra_compile_args=["-w"]),
    Extension("coalescent_lib", ["coalescent_lib.pyx"], extra_compile_args=["-w"]),
    Extension("dtwf_lib", ["dtwf_lib.pyx"], extra_compile_args=["-w"]),
]
setup(ext_modules=cythonize(extensions))

# Linking the Mac Module to a general library
if system == "Mac":
    call(["mv", "moran_lib.cpython-37m-darwin.so", "moran_lib.so"])
    call(["mv", "coalescent_lib.cpython-37m-darwin.so", "coalescent_lib.so"])
    call(["mv", "dtwf_lib.cpython-37m-darwin.so", "dtwf_lib.so"])

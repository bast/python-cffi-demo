import os
import sys
from subprocess import Popen, PIPE
from cffi import FFI

ffi = FFI()

interface = Popen(['cc', '-E', 'example.h'],
                  stdout=PIPE).communicate()[0].decode("utf-8")
ffi.cdef(interface)

if sys.platform == "darwin":
    suffix = 'dylib'
else:
    suffix = 'so'

c_lib = ffi.dlopen(os.path.join('build', 'libc_example.{}'.format(suffix)))
fortran_lib = ffi.dlopen(os.path.join('build', 'libfortran_example.{}'.format(suffix)))

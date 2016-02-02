"""
Python handle to example library.
"""

import os
import sys
import subprocess
from cffi import FFI

BUILD_DIR = os.path.abspath(os.path.dirname(__file__))

ffi = FFI()

ffi.cdef(
    subprocess.Popen(
        [
            'cc',
            '-E',
            '-DEXAMPLE_API=',
            '-DEXAMPLE_NOINCLUDE',
            os.path.join(BUILD_DIR, 'include', 'example.h')
        ],
        stdout=subprocess.PIPE).communicate()[0])

if sys.platform == "darwin":
    suffix = 'dylib'
else:
    suffix = 'so'

lib = ffi.dlopen(os.path.join(BUILD_DIR, 'lib', 'libexample.%s' % suffix))

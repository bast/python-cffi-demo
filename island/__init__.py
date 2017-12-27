import os
from .cffi_helpers import get_lib_handle
from .pi import approximate_pi as approximate_pi_python

__all__ = [
    'approximate_pi_python',
    'approximate_pi_c',
    'approximate_pi_fortran',
]

_this_path = os.path.dirname(os.path.realpath(__file__))

_library_dir = os.getenv('PI_LIBRARY_DIR')
if _library_dir is None:
    _library_dir = os.path.join(_this_path, 'lib')

_include_dir = os.getenv('PI_INCLUDE_DIR')
if _include_dir is None:
    _include_dir = os.path.join(_this_path, 'include')

_lib_c = get_lib_handle(
    ['-DPI_API='],
    'pi.h',
    'pi_cpp',
    _library_dir,
    _include_dir
)

approximate_pi_c = _lib_c.approximate_pi_c

_lib_fortran = get_lib_handle(
    ['-DPI_API='],
    'pi.h',
    'pi_fortran',
    _library_dir,
    _include_dir
)

approximate_pi_fortran = _lib_fortran.approximate_pi_fortran

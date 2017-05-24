import os
from .cffi_helpers import get_lib_handle
from .example import approximate_pi as approximate_pi_python

__all__ = [
    'approximate_pi_python',
    'approximate_pi_c',
    'approximate_pi_fortran',
]

_this_path = os.path.dirname(os.path.realpath(__file__))
_include_dir = _this_path

_build_dir = os.getenv('PI_BUILD_DIR')
if _build_dir is None:
    _build_dir = _this_path
else:
    _build_dir = os.path.join(_build_dir, 'lib')

_lib_c = get_lib_handle(
    ['-DPI_API='],
    'pi.h',
    'pi_cpp',
    _build_dir,
    _include_dir
)

approximate_pi_c = _lib_c.approximate_pi_c

_lib_fortran = get_lib_handle(
    ['-DPI_API='],
    'pi.h',
    'pi_f90',
    _build_dir,
    _include_dir
)

approximate_pi_fortran = _lib_fortran.approximate_pi_fortran

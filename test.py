from example import c_lib, fortran_lib
from pi import approximate_pi


def test_c_code():
    l = [1.0, 2.0, 3.0]
    s = c_lib.c_sum(len(l), l)
    assert s == 6.0


def test_fortran_code():
    l = [1.0, 2.0, 3.0]
    d = fortran_lib.fortran_dot(len(l), l, l)
    assert d == 14.0


def test_pi():
    pi = approximate_pi(seed=0, num_points=1000000)
    assert abs(pi - 3.141593) < 1.0e-3

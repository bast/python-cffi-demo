from example import c_lib, fortran_lib


def test_c_code():
    l = [1.0, 2.0, 3.0]
    s = c_lib.c_sum(len(l), l)
    assert s == 6.0


def test_fortran_code():
    l = [1.0, 2.0, 3.0]
    d = fortran_lib.fortran_dot(len(l), l, l)
    assert d == 14.0

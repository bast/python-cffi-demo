#from example import c_lib, fortran_lib
from pi import approximate_pi


def test_pi():
    pi = approximate_pi(num_points=1000000)
    assert abs(pi - 3.141593) < 1.0e-3

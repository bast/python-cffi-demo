from pi import approximate_pi_python


def test_pi():
    pi = approximate_pi_python(num_points=1000000)
    assert abs(pi - 3.141593) < 1.0e-3

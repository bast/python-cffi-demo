import time
import pi


def test_pi_python():
    num_points = 1000000
    result = pi.approximate_pi_python(num_points)
    assert abs(result - 3.141593) < 2.0e-3


def test_pi_c():
    num_points = 1000000
    result = pi.approximate_pi_c(num_points)
    assert abs(result - 3.141593) < 2.0e-3


def test_pi_fortran():
    num_points = 1000000
    result = pi.approximate_pi_fortran(num_points)
    assert abs(result - 3.141593) < 2.0e-3


def print_timings():
    num_points = 5000000

    for (lang, function) in [('python', pi.approximate_pi_python),
                             ('c', pi.approximate_pi_c),
                             ('fortran', pi.approximate_pi_fortran)]:

        t0 = time.clock()
        result = function(num_points)
        time_spent = time.clock() - t0

        print('{0:7s} pi={1:.5f} time spent: {2:.3f} sec'.format(lang, result, time_spent))


if __name__ == '__main__':
    print_timings()

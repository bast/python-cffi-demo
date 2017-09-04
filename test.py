import time
import island


num_points = 2000000
pi_reference = 3.141593


def test_pi_python():
    result = island.approximate_pi_python(num_points)
    assert abs(result - pi_reference) < 2.0e-3


def test_pi_c():
    result = island.approximate_pi_c(num_points)
    assert abs(result - pi_reference) < 2.0e-3


def test_pi_fortran():
    result = island.approximate_pi_fortran(num_points)
    assert abs(result - pi_reference) < 2.0e-3


def print_timings():
    print('num points: {0}'.format(num_points))

    for (lang, function) in [('python', island.approximate_pi_python),
                             ('c', island.approximate_pi_c),
                             ('fortran', island.approximate_pi_fortran)]:
        t0 = time.clock()
        result = function(num_points)
        time_spent = time.clock() - t0

        print('{0:7s} pi={1:.5f} time spent: {2:.3f} sec'.format(lang, result, time_spent))


if __name__ == '__main__':
    print_timings()

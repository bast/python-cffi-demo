import time

import pi

num_points = 5000000

for (lang, function) in [('python', pi.approximate_pi_python),
                         ('c', pi.approximate_pi_c),
                         ('fortran', pi.approximate_pi_fortran)]:

    t0 = time.clock()
    result = function(num_points)
    time_spent = time.clock() - t0

    print('{0:7s} pi={1:.5f} time spent: {2:.3f} sec'.format(lang, result, time_spent))

import random


def _distance_to_origin_squared(x, y):
    return x*x + y*y


def approximate_pi(seed, num_points):

    random.seed(seed)
    num_inside = 0

    for _ in range(num_points):
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 1.0)
        if _distance_to_origin_squared(x, y) < 1.0:
            num_inside += 1

    # we multiply by 4 to get the full circle
    # from the 4 segments
    return 4.0*num_inside/float(num_points)

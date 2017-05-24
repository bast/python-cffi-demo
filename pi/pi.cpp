// provides rand and RAND_MAX
#include <cstdlib>

#include "pi.h"

double distance_to_origin_squared(const double x, const double y)
{
    return x * x + y * y;
}

double approximate_pi_c(const int num_points)
{
    int num_inside = 0;

    for (int i = 0; i < num_points; i++)
    {
        double x = ((double)rand() / (RAND_MAX));
        double y = ((double)rand() / (RAND_MAX));
        if (distance_to_origin_squared(x, y) < 1.0)
        {
            num_inside++;
        }
    }

    // we multiply by 4 to get the full circle
    // from the 4 segments
    return 4.0 * num_inside / ((double)num_points);
}

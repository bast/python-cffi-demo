#include "example.h"

double c_sum(const int n,
             const double u[])
{
    double s = 0.0;
    int i;
    for (i = 0; i < n; i++)
    {
        s += u[i];
    }
    return s;
}

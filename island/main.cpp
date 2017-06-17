#include <stdio.h>

#include "pi.h"

int main()
{
    printf("pi computed by c = %f\n", approximate_pi_c(1000000));
//  printf("pi computed by fortran = %f\n", approximate_pi_fortran(1000000));

    return 0;
}

#include <stdio.h>

#include "pi.h"

int main()
{
    printf("pi computed by c = %f\n", approximate_pi(1000000));

    return 0;
}

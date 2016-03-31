#ifndef EXAMPLE_H_INCLUDED
#define EXAMPLE_H_INCLUDED

/* defined in c code */
double c_sum(const int n,
             const double u[]);

/* defined in fortran code */
double fortran_dot(const int n,
                   const double u[],
                   const double v[]);

#endif /* EXAMPLE_H_INCLUDED */

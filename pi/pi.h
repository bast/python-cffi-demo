#ifndef PI_H_INCLUDED
#define PI_H_INCLUDED

#ifndef PI_API
#include "pi_export.h"
#define PI_API PI_EXPORT
#endif

#ifdef __cplusplus
extern "C" {
#endif

PI_API
double approximate_pi(const int num_points);

#ifdef __cplusplus
}
#endif

#endif /* PI_H_INCLUDED */

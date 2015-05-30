#include "gtest/gtest.h"
#include "example.h"

TEST(example, subtract)
{
    example_context_t *context = example_new();
    double res = example_subtract(context, 1.0, 2.0);
    example_free(context);
    ASSERT_NEAR(res, -1.0, 1.0e-11);
}

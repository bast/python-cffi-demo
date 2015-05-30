#include "gtest/gtest.h"
#include "example.h"

TEST(example, add)
{
    example_context_t *context = example_new();
    double res = example_add(context, 1.0, 2.0);
    example_free(context);
    ASSERT_NEAR(res, 3.0, 1.0e-11);
}

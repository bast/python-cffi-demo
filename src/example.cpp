
#include "example.h"

#define AS_TYPE(Type, Obj) reinterpret_cast<Type *>(Obj)
#define AS_CTYPE(Type, Obj) reinterpret_cast<const Type *>(Obj)


namespace example {
    class Context {
    public:
        Context();
        ~Context();

        const char *get_string() const;
        double add(const double f1, const double f2) const;
        double subtract(const double f1, const double f2) const;
        double multiply(const double f1, const double f2) const;
    private:
        int *foo;
    };
}


example_context_t *example_new()
{
    return AS_TYPE(example_context_t, new example::Context());
}
example::Context::Context()
{
    foo = new int[5];
}


void example_free(example_context_t *context)
{
    if (!context) return;
    delete AS_TYPE(example::Context, context);
}
example::Context::~Context()
{
    delete[] foo;
}


const char *example_get_string(const example_context_t *context)
{
    return AS_CTYPE(example::Context, context)->get_string();
}
const char *example::Context::get_string() const
{
   return "raboof!";
}


double example_add(const example_context_t *context, const double f1, const double f2)
{
    return AS_CTYPE(example::Context, context)->add(f1, f2);
}
double example::Context::add(const double f1, const double f2) const
{
    return f1 + f2;
}


double example_subtract(const example_context_t *context, const double f1, const double f2)
{
    return AS_CTYPE(example::Context, context)->subtract(f1, f2);
}
double example::Context::subtract(const double f1, const double f2) const
{
    return f1 - f2;
}


double example_multiply(const example_context_t *context, const double f1, const double f2)
{
    return AS_CTYPE(example::Context, context)->multiply(f1, f2);
}
double example::Context::multiply(const double f1, const double f2) const
{
    return f1*f2;
}

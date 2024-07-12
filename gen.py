from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
void fun(int n, int *res, ...);
""")

ffibuilder.set_source("_fun", """
#include <stdarg.h>
#include <stdio.h>

void fun(int n, int *res, ...) {
    va_list args;
    va_start(args, res);
    *res = *va_arg(args, int*);
    va_end(args);
}
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

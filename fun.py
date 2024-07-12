from _fun import ffi, lib

num = 42
res = ffi.new("int*")
arg = ffi.cast("int", num)
lib.fun(0, res, arg)
print(res[0], "==", num)

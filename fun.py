from _fun import ffi, lib

res = ffi.new("int*")
arg = ffi.new("int*", 42)
lib.fun(0, res, arg)
assert res[0] == arg[0]
print("success")

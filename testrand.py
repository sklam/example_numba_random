from numba import jit


######## Using the old numba random library


from randomlibrary import rk_double, rk_gauss, state_value


@jit
def foo():
    for i in range(10):
        x = rk_double(state_value)
        if x > 0.2:
            return rk_gauss(state_value)


print(foo())


######## Wrapping rand() from libc
import ctypes

libc = ctypes.CDLL(None)
libc_rand = libc.rand
libc_srand = libc.srand

libc_rand.argtypes = []
libc_rand.restype = ctypes.c_double

libc_srand.argtypes = [ctypes.c_uint]
libc_srand.restype = None


@jit
def bar(seed):
    libc_srand(seed)
    return libc_rand()


print(bar(0))





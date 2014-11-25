example_numba_random
====================

This contains example code for doing random number generation in numba.  

The testrand.py script contains:

1. Reusing old and removed numba.random module.  The module is renamed and modified to `randomlibrary`.  It uses numpy's internal shared library for the random number generation.

2. Using ctypes to wrap libc's rand() and srand() for random number generation.


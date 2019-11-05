#!/usr/bin/env python3

import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])
print(A)

# You can also use the numpy.matrix type, which is a specialist subclass of array (although it's not recommended)
M = np.matrix([[1, 2, 3],
               [4, 5, 6]])
print(M)

B = np.array([[6, 5, 4],
              [3, 2, 1]])
print(A + B)

print(A - B)

# Negative matrix - just invert the sign of each element
print(-A)

# Matrix transpose
print(A.T)

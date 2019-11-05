#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

v = np.array([2, 1])

w = 2 * v
print(w)

# Plot v & w
vecs = np.array([v, w])
origin = [0], [0]
plt.grid()
plt.ticklabel_format(style='sci', axis='both', scilimits=(0, 0))
plt.quiver(*origin, vecs[1], vecs[0], color=['r', 'b'], scale=10)
plt.show()

s = np.array([-3, 2])
dp = np.dot(v, s)
print(dp)

p = np.array([2, 3, 1])
q = np.array([1, 2, -2])
cp = np.cross(p, q)
print(cp)

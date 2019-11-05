#!/usr/bin/env python3

import math
import numpy as np
import matplotlib.pyplot as plt

# We'll use a numpy array for our vector
v = np.array([2, 1])

# Get the magnitude
print('Mag ' + str(v) + ': ' + str(math.sqrt(v[0] ** 2 + v[1] ** 2)))
print('Mag ' + str(v) + ': ' + str(np.linalg.norm(v)))  # handles multi-dimension arrays

# And the direction
print('Dir ' + str(v) + ': ' + str(np.degrees(np.arctan2(v[1], v[0]))))

s = np.array([-3, 2])
z = v + s

# Plot v, s, and v + s
vecs = np.array([v, s, z])
origin = [0], [0]
plt.axis('equal')
plt.grid()
plt.ticklabel_format(style='sci', axis='both', scilimits=(0, 0))
plt.quiver(*origin, vecs[:, 0], vecs[:, 1], color=['r', 'b', 'g'], scale=10)
plt.show()

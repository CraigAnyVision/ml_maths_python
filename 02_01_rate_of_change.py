#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


# Linear function
def q(x):
    return 2 * x + 1


# Non-linear (quadratic) function
def r(x):
    return x ** 2 + x


# Create an array of x values from 0 to 10
x = np.array(range(0, 11))

# Set up the graph
plt.xlabel('Seconds')
plt.ylabel('Meters')
plt.grid()

# Set up the graph
plt.xlabel('Seconds')
plt.ylabel('Meters')
plt.xticks(range(0, 11, 1))
plt.yticks(range(0, 22, 1))
plt.grid()

# Plot x against q(x)
plt.plot(x, q(x), color='green')
plt.show()

# Create an array for the secant line
s = np.array([2, 7])

# Calculate rate of change
x1 = s[0]
x2 = s[-1]
y1 = r(x1)
y2 = r(x2)
a = (y2 - y1) / (x2 - x1)

# Plot x against r(x)
plt.plot(x, r(x), color='green')

# Plot the secant line
plt.plot(s, r(s), color='magenta')
plt.annotate('Average Velocity =' + str(a) + ' m/s', ((x2 + x1) / 2, (y2 + y1) / 2))

plt.show()

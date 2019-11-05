#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


# Define function g
def g(x):
    if x != 0:
        return (12 / (2 * x)) ** 2


# Plot output from function g

# Create an array of x values from -100 to 100
x = range(-100, 101)

# Get the corresponding y values from the function
y = [g(a) for a in x]

# Set up the graph
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid()

# Plot x against g(x)
plt.plot(x, y, color='purple')

# plot an empty circle to show the undefined point
plt.plot(0, g(0.0000001), color='purple', marker='o', markerfacecolor='w', markersize=8)

plt.show()

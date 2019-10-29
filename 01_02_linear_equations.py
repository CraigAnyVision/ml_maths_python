#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt

# Create a dataframe with an x column containing values from -10 to 10
df = pd.DataFrame({'x': range(-10, 11)})

# Add a y column by applying the solved equation to x
df['y'] = (3 * df['x'] - 4) / 2

# Display the dataframe
print(df)

plt.plot(df.x, df.y, color="grey", marker="o")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

# Add axis lines for 0,0
plt.axhline()
plt.axvline()
plt.annotate('x-intercept', (1.333, 0))
plt.annotate('y-intercept', (0, -2))

# Set the slope (Δy / Δx)
m = (df['y'][10] - df['y'][16]) / (df['x'][10] - df['x'][16])

# Get the y-intercept
yInt = -2

# Plot the slope from the y-intercept for 1x
mx = [0, 1]
my = [yInt, yInt + m]
plt.plot(mx, my, color='red', lw=5)

plt.show()

# Slope intercept form: y = mx + b
# m is the slope and b is the y-intercept
m = 1.5
b = -2

# Create a new dataframe with an x column containing values from -10 to 10
df2 = pd.DataFrame({'x': range(-10, 11)})

# Add a y column by applying the slope-intercept equation to x
df2['y'] = m * df2['x'] + b

# Display the dataframe
print(df2)

# Plot the line
plt.plot(df2.x, df2.y, color="grey")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline()
plt.axvline()

# Label the y-intercept
plt.annotate('y-intercept', (0, yInt))

# Plot the slope from the y-intercept for 1x
mx = [0, 1]
my = [yInt, yInt + m]
plt.plot(mx, my, color='red', lw=5)

plt.show()

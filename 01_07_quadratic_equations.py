#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import math


def plot_quadratic_1():
    # Create a dataframe with an x column containing values to plot
    df = pd.DataFrame({'x': range(-9, 9)})

    # Add a y column by applying the quadratic equation to x
    df['y'] = 2 * df['x'] ** 2 + 2 * df['x'] - 4  # y = 2x^2 + 2x - 4

    # Plot the line
    plt.plot(df.x, df.y, color="grey")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axhline()
    plt.axvline()
    plt.show()


def plot_quadratic_2():
    df2 = pd.DataFrame({'x': range(-8, 12)})

    # Add a y column by applying the quadratic equation to x
    df2['y'] = -2 * df2['x'] ** 2 + 6 * df2['x'] + 7  # y = -2x^2 + 6x + 7

    # Plot the line
    plt.plot(df2.x, df2.y, color="grey")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axhline()
    plt.axvline()
    plt.show()


def plot_parabola(a, b, c):
    # get the x value for the line of symmetry
    vx = (-1 * b) / (2 * a)

    # get the y value when x is at the line of symmetry
    vy = a * vx ** 2 + b * vx + c

    # Create a dataframe with an x column containing values from x-10 to x+10
    minx = int(vx - 10)
    maxx = int(vx + 11)
    df = pd.DataFrame({'x': range(minx, maxx)})

    # Add a y column by applying the quadratic equation to x
    df['y'] = a * df['x'] ** 2 + b * df['x'] + c

    # get min and max y values
    miny = df.y.min()
    maxy = df.y.max()

    # Plot the line
    plt.plot(df.x, df.y, color="grey")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axhline()
    plt.axvline()

    # plot the line of symmetry
    sx = [vx, vx]
    sy = [miny, maxy]
    plt.plot(sx, sy, color='magenta')

    # Annotate the vertex
    plt.scatter(vx, vy, color="red")
    plt.annotate('vertex', (vx, vy), xytext=(vx - 1, (vy + 5) * np.sign(a)))

    plt.show()


def plot_parabola_points():
    # Assign the calculated x values
    x1 = -2
    x2 = 1

    # Create a dataframe with an x column containing some values to plot
    df = pd.DataFrame({'x': range(x1 - 5, x2 + 6)})

    # Add a y column by applying the quadratic equation to x
    df['y'] = 2 * (df['x'] - 1) * (df['x'] + 2)

    # Get x at the line of symmetry (halfway between x1 and x2)
    vx = (x1 + x2) / 2

    # Get y when x is at the line of symmetry
    vy = 2 * (vx - 1) * (vx + 2)

    # get min and max y values
    miny = df.y.min()
    maxy = df.y.max()

    # Plot the line
    plt.plot(df.x, df.y, color="grey")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axhline()
    plt.axvline()

    # Plot calculated x values for y = 0
    plt.scatter([x1, x2], [0, 0], color="green")
    plt.annotate('x1', (x1, 0))
    plt.annotate('x2', (x2, 0))

    # plot the line of symmetry
    sx = [vx, vx]
    sy = [miny, maxy]
    plt.plot(sx, sy, color='magenta')

    # Annotate the vertex
    plt.scatter(vx, vy, color="red")
    plt.annotate('vertex', (vx, vy), xytext=(vx - 1, (vy - 5)))

    plt.show()


def square_root_method():
    y = 0
    x1 = int(- math.sqrt(y + 12 / 3))
    x2 = int(math.sqrt(y + 12 / 3))

    # Create a dataframe with an x column containing some values to plot
    df = pd.DataFrame({'x': range(x1 - 10, x2 + 11)})

    # Add a y column by applying the quadratic equation to x
    df['y'] = 3 * df['x'] ** 2 - 12

    # Get x at the line of symmetry (halfway between x1 and x2)
    vx = (x1 + x2) / 2

    # Get y when x is at the line of symmetry
    vy = 3 * vx ** 2 - 12

    # get min and max y values
    miny = df.y.min()
    maxy = df.y.max()

    # Plot the line
    plt.plot(df.x, df.y, color="grey")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axhline()
    plt.axvline()

    # Plot calculated x values for y = 0
    plt.scatter([x1, x2], [0, 0], color="green")
    plt.annotate('x1', (x1, 0))
    plt.annotate('x2', (x2, 0))

    # plot the line of symmetry
    sx = [vx, vx]
    sy = [miny, maxy]
    plt.plot(sx, sy, color='magenta')

    # Annotate the vertex
    plt.scatter(vx, vy, color="red")
    plt.annotate('vertex', (vx, vy), xytext=(vx - 1, (vy - 20)))

    plt.show()


def completing_the_square_method():
    x1 = int(- math.sqrt(16) - 3)
    x2 = int(math.sqrt(16) - 3)

    # Create a dataframe with an x column containing some values to plot
    df = pd.DataFrame({'x': range(x1 - 10, x2 + 11)})

    # Add a y column by applying the quadratic equation to x
    df['y'] = ((df['x'] + 3) ** 2) - 16

    # Get x at the line of symmetry (halfway between x1 and x2)
    vx = (x1 + x2) / 2

    # Get y when x is at the line of symmetry
    vy = ((vx + 3) ** 2) - 16

    # get min and max y values
    miny = df.y.min()
    maxy = df.y.max()

    # Plot the line
    plt.plot(df.x, df.y, color="grey")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axhline()
    plt.axvline()

    # Plot calculated x values for y = 0
    plt.scatter([x1, x2], [0, 0], color="green")
    plt.annotate('x1', (x1, 0))
    plt.annotate('x2', (x2, 0))

    # plot the line of symmetry
    sx = [vx, vx]
    sy = [miny, maxy]
    plt.plot(sx, sy, color='magenta')

    # Annotate the vertex
    plt.scatter(vx, vy, color="red")
    plt.annotate('vertex', (vx, vy), xytext=(vx - 1, (vy - 10)))

    plt.show()


def plot_parabola_from_vertex_form(a, h, k):
    # Create a dataframe with an x column a range of x values to plot
    df = pd.DataFrame({'x': range(h - 10, h + 11)})

    # Add a y column by applying the quadratic equation to x
    df['y'] = (a * (df['x'] - h) ** 2) + k

    # get min and max y values
    miny = df.y.min()
    maxy = df.y.max()

    # calculate y when x is 0 (h+-h)
    y = a * (0 - h) ** 2 + k

    # Plot the line
    plt.plot(df.x, df.y, color="grey")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axhline()
    plt.axvline()

    # Plot calculated y values for x = 0 (h-h and h+h)
    plt.scatter([h - h, h + h], [y, y], color="green")
    plt.annotate(str(h - h) + ',' + str(y), (h - h, y))
    plt.annotate(str(h + h) + ',' + str(y), (h + h, y))

    # plot the line of symmetry (x = h)
    sx = [h, h]
    sy = [miny, maxy]
    plt.plot(sx, sy, color='magenta')

    # Annotate the vertex (h,k)
    plt.scatter(h, k, color="red")
    plt.annotate('v=' + str(h) + ',' + str(k), (h, k), xytext=(h - 1, (k - 10)))

    plt.show()


def plot_parabola_from_formula(a, b, c):
    # Get vertex
    print('CALCULATING THE VERTEX')
    print('vx = -b / 2a')

    nb = -b
    a2 = 2 * a
    print('vx = ' + str(nb) + ' / ' + str(a2))

    vx = -b / (2 * a)
    print('vx = ' + str(vx))

    print('\nvy = ax^2 + bx + c')
    print('vy =' + str(a) + '(' + str(vx) + '^2) + ' + str(b) + '(' + str(vx) + ') + ' + str(c))

    avx2 = a * vx ** 2
    bvx = b * vx
    print('vy =' + str(avx2) + ' + ' + str(bvx) + ' + ' + str(c))

    vy = avx2 + bvx + c
    print('vy = ' + str(vy))

    print('\nv = ' + str(vx) + ',' + str(vy))

    # Get +x and -x (showing intermediate calculations)
    print('\nCALCULATING -x AND +x FOR y=0')
    print('x = -b +- sqrt(b^2 - 4ac) / 2a')

    b2 = b ** 2
    ac4 = 4 * a * c
    print('x = ' + str(nb) + '+-sqrt(' + str(b2) + ' - ' + str(ac4) + ')/' + str(a2))

    sr = math.sqrt(b2 - ac4)
    print('x = ' + str(nb) + ' +- ' + str(sr) + ' / ' + str(a2))
    print('-x = ' + str(nb) + ' - ' + str(sr) + ' / ' + str(a2))
    print('+x = ' + str(nb) + ' + ' + str(sr) + ' / ' + str(a2))

    posx = (nb + sr) / a2
    negx = (nb - sr) / a2
    print('-x = ' + str(negx))
    print('+x = ' + str(posx))

    print('\nPLOTTING THE PARABOLA')

    # Create a dataframe with an x column a range of x values to plot
    df = pd.DataFrame({'x': range(round(vx) - 10, round(vx) + 11)})

    # Add a y column by applying the quadratic equation to x
    df['y'] = a * df['x'] ** 2 + b * df['x'] + c

    # get min and max y values
    miny = df.y.min()
    maxy = df.y.max()

    # Plot the line
    plt.plot(df.x, df.y, color="grey")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axhline()
    plt.axvline()

    # Plot calculated x values for y = 0
    plt.scatter([negx, posx], [0, 0], color="green")
    plt.annotate('-x=' + str(negx) + ',' + str(0), (negx, 0), xytext=(negx - 3, 5))
    plt.annotate('+x=' + str(posx) + ',' + str(0), (posx, 0), xytext=(posx - 3, -10))

    # plot the line of symmetry
    sx = [vx, vx]
    sy = [miny, maxy]
    plt.plot(sx, sy, color='magenta')

    # Annotate the vertex
    plt.scatter(vx, vy, color="red")
    plt.annotate('v=' + str(vx) + ',' + str(vy), (vx, vy), xytext=(vx - 1, vy - 10))

    plt.show()


# plot_quadratic_1()
# plot_quadratic_2()
# plot_parabola(2, 2, -4)
# plot_parabola(-2, 3, 5)
# plot_parabola_points()
# square_root_method()
# completing_the_square_method()
# plot_parabola_from_vertex_form(2, 4, -30)
# plot_parabola_from_vertex_form(3, -1, -1)
# plot_parabola_from_formula (2, -16, 2)
plot_parabola(3, -12, 4)

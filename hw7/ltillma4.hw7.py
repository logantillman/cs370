#!/usr/bin/env python3

# Author: Logan Tillman
# NetID: Ltillma4
# Hw7

from newtonRaphson2 import *
from math import sin, pi
import numpy as np
import matplotlib.pyplot as plt

#  R = x[0] / (1 + x[1])
#  Theta = (pi/2.0 - x[2]) * 180.0 / pi
#  C = 6870 - x[0]/(1+x[1]*sin(-pi/6 + x[2]))
#  e = 6728 - x[0]/(1+x[1]*sin(0 + x[2]))
#  alpha = 6615 - x[0]/(1+x[1]*sin(pi/6 + x[2]))
#  Name: Logan Tillman
#  Assignment: Hw7

def F(x):
    F = zeros((len(x)), dtype=float64)
    F[0] = 6870 - x[0]/(1+x[1]*sin(-pi/6 + x[2]))   # Defining C
    F[1] = 6728 - x[0]/(1+x[1]*sin(0 + x[2]))       # Defining e
    F[2] = 6615 - x[0]/(1+x[1]*sin(pi/6 + x[2]))    # Defining alpha
    return F

# Initial guess
x = np.array([6800, 0.5, 0])

# Complete the call to the N-R method to solve for unknowns
x = newtonRaphson2(F, x)

# Print the solution vector x from N-R
print()
np.set_printoptions(precision = 3)
print('[ C  e  alpha] = ' + np.array_str(x))

# Calculate minimum trajectory and angle using components of x
minTheta = (pi/2.0 - x[2]) * 180.0 / pi
minR = x[0] / (1 + x[1])

# Print minimum trajectory results
print('Minimum trajectory = %.3f km' % minR)
print('Angle at which minimum trajectory occurs = %.3f degrees' % minTheta)
print()

#-------------------------------------------------------------
# Outputs for verification:
# C  e  alpha] = [  6.819e+03   4.060e-02   3.408e-01]
# Minimum trajectory = 6553.239 km
# Angle at which minimum trajectory occurs = 70.475 degrees
#-------------------------------------------------------------

# Create arrays of points spaced every 0.01 radians around the satellite orbit
# (theta) and their respective trajectories (R)

theta = np.arange(0, 2*pi, 0.01)            # theta and R are arrays now
R = x[0] / (1 + x[1]*np.sin(theta + x[2]))

# Plot orbit and minimum trajectory point

ax = plt.subplot(111, polar = True)
ax.plot(theta, R, color = 'r', linewidth = 2, label = 'Path')
ax.plot(minTheta, minR, 'bo', label = 'Min')
ax.legend(numpoints = 1)
ax.grid(True)
ax.set_title("Satellite path")
plt.show()
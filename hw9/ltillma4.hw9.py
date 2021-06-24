#!/usr/bin/env python3

# Author: Logan Tillman
# NetID: Ltillma4
# Hw9

# The Romberg Integration is a combination of the Trapezoidal Rule
# and Richardson extrapolation to improve the estimates of integral approximation

from romberg import *
from numpy import *
from math import e
import matplotlib.pyplot as plt

def f(x):
  if x == 0: return 0
  else: return  (x**4 * e**x)/((e**x - 1)**2)

u = arange(0,1.01,0.05)
print ("    u\t   g(u)")
gu = [] #list that will contain all of g(u)s (y-coordinates for your plot)

for i in u:
  if i == 0: g = 0.0;
  else:
    I,nPanels = romberg(f, 0, 1/i)  # perform romberg integration on f here (get result in
                     # I, nPanels is the number of panels used but is not
                     # used for output.
    g = i**3 * I          # evaluate g(i) here
  print ('{:6.2f}{:13.6f}'.format(i,g))
  gu.append(g)

# Creating the plot
plt.plot(u, gu)
plt.xlim(0.0, 1.0)
plt.ylim(0.00, 0.35)
plt.title("Problem 6.1.14")
plt.xlabel("u")
plt.ylabel("g(u)")
plt.show()
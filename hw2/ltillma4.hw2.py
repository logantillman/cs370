#!/usr/bin/env python3

# Author: Logan Tillman
# NetID: Ltillma4
# Hw2

from numpy import zeros, ones, array, float64, inf
from numpy import linalg
from LUdecomp import *

norm = linalg.norm

TOL = 1.E-6
err = 0
n = 0
while err < TOL:
  n +=1
  a = zeros((n,n),dtype=float64)  
  b = zeros((n),dtype=float64)  
  soln = ones((n), dtype=float64)
  
  for i in range(n):    
    for j in range(n):      
      a[i,j] = 1.0 / ((i + 1) + (j + 1) - 1)  # Creating the Hilbert Matrix
      b[i] = sum(a[i])  # Calculating the b vector
    
  a = LUdecomp(a)
  b = LUsolve(a,b)  # Solving the matrix and storing it in the b variable

  print("\n", n, " equations. ", "The solution is:\n", b)
  err = norm(b-soln, ord=inf)  
  print("Error (inf-norm of difference)): ", err)

print("^^^(Greater than TOL = ", TOL, ")^^^\n")
print("********************************************\n")
print("Max number of equations while error remains less than ", TOL, " is: ", n-1, "\n")
print("********************************************")
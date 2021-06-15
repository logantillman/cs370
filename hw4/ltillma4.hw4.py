#!/usr/bin/env python3

# Author: Logan Tillman
# NetID: Ltillma4 
# Hw4

from numpy import zeros,array,linalg
from conjGrad import *

def Ax(v):
  Ax = zeros((9))*1.0

  # Defining the matrix A
  A = zeros((9,9))*1.0
  A[0] = [-4, 1, 0, 1, 0, 0, 0, 0, 0]
  A[1] = [1, -4, 1, 0, 1, 0, 0, 0, 0]
  A[2] = [0, 1, -4, 0, 0, 1, 0, 0, 0]
  A[3] = [1, 0, 0, -4, 1, 0, 1, 0, 0]
  A[4] = [0, 1, 0, 1, -4, 1, 0, 1, 0]
  A[5] = [0, 0, 1, 0, 1, -4, 0, 0, 1]
  A[6] = [0, 0, 0, 1, 0, 0, -4, 1, 0]
  A[7] = [0, 0, 0, 0, 1, 0, 1, -4, 1]
  A[8] = [0, 0, 0, 0, 0, 1, 0, 1, -4]

  # Calculating the matrix-vector product, only looking at the non-zero numbers in A
  for i in range(len(A)):
    sum = 0
    for j in range(len(A[i])):
      if A[i, j] == 0:
        continue
      sum += (A[i, j] * v[j])
    Ax[i] = sum

  return Ax

b = array([0,0,100,0,0,100,200,200,300])*(-1.0)
x = zeros((9))*1.0
tol = 1e-06

# Calling conjGrad, giving it the matrix-vector product function
s1,numIter = conjGrad(Ax, x, b, tol)
print("\nThe solution is:\n",s1)
print("\nNumber of iterations =",numIter, "using Tol: ", 1e-06)

print("\n CG Convergence Test")
print("Iterations   Tolerance")

tolerances = [1.e-02, 1.e-04, 1.e-06, 1.e-08, 1.e-10, 1.e-12, 1.e-14, 1.e-16]

# Printing the number of iterations for each tolerance
for tolerance in tolerances:
  sol, numIt = conjGrad(Ax, x, b, tolerance)
  print('    ', numIt, '       ', tolerance)

# Calculating and printing the error? maybe?
sol1 = conjGrad(Ax, x, b, 1.e-06)
sol2 = conjGrad(Ax, x, b, 1.e-16)
err = 0
for i, sol in enumerate(sol1[0]):
  err += abs(sol1[0][i] - sol2[0][i])

print("\nError between vectors obtained with tol=1e-06 and tol=1e-16: ", err, "\n")
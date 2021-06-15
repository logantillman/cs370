#!/usr/bin/env python3

# prob2-3-19 (hwk #4)
#
#  Problem 2.3.19 (pg. 101)
#
#  1) Implement the Ax(v) function below so that it will initialize
#     and return the matrix-vector product Ax, where A is given at
#     the top of page 101 in the textbook.
#  
#  2) Use the provided conjGrad.py module to solve the system described
#     in problem #19 (uncomment and fill in the '??' lines and provide
#     the requested loop and final error difference).
#
# The correct solution is:
#
# [ 21.42857143 38.39285714  57.14285714   47.32142857   75.
#   90.17857143 92.85714286 124.10714286 128.57142857]
#
########################################################################

from numpy import zeros,array,linalg
from conjGrad import *

# Refer to pg. 101 for what the matrix Ax should be

def Ax(v):
  Ax = zeros((9))*1.0

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
s1,numIter = conjGrad(Ax, x, b, tol)
print("\nThe solution is:\n",s1)
print("\nNumber of iterations =",numIter, "using Tol: ", 1e-06)

print("\n CG Convergence Test")
print("Iterations   Tolerance")
#
# Create a loop here to call conjGrad with these tolerances and obtain/print the iteration
# count with each tolerance used:  1.e-02, 1.e-04, 1.e-06, 1.e-08, 1.e-10, 1.e-12, 1.e-14, 1.e-16
# tolerances = [1.e-06]
tolerances = [1.e-02, 1.e-04, 1.e-06, 1.e-08, 1.e-10, 1.e-12, 1.e-14, 1.e-16]
for tolerance in tolerances:
  sol, numIt = conjGrad(Ax, x, b, tolerance)
  print('    ', numIt, '       ', tolerance)

# Finally, print the error between the solutions using the 1.e-06 and 1.e-16 tolerances

sol1 = conjGrad(Ax, x, b, 1.e-06)
sol2 = conjGrad(Ax, x, b, 1.e-16)

#FIXME Complete this last part
print("\nError between vectors obtained with tol=1e-06 and tol=1e-16: ", sol1 - sol2,"\n")
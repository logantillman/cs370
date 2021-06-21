#!/usr/bin/env python3
#
# Template for Problem 10 from Problem Set 3.2
#
# Insert a comment block describing the problem and curve fitting
# approach deployed.  Also, be sure your name and assignment
# number are included in your comments.
#
# ???
# ???
# ???
# ???
# ???
# ???

from numpy import array,zeros
from polyFit import *
import pylab

def evalPoly(c,x): # c stores coefficients for polynomial
    m = len(c) - 1 # (copied from polyFit module)
    p = c[m]
    for j in range(m):
        p = p*x + c[m-j-1]
    return p

xData = array(???) // xData array contains the years
yData = array(???) // yData array contains the efficiencies (as percentages)

minsdev=float("inf")
minpoly=0
n=len(xData)
print('Degree  Stdev   2000P')
for m in range(1,6):   # Try m=1,2,3,4,5 (degree of polynomial)
    ys=zeros((n),dtype='float') # initialize y-coordinates for polynomial curve

    coeff = ??? # get coefficients for n-th degree polynomial
    stdev = ??? # get stdev of the error in the fit
    proj  = ??? # evaluate the polynomial at year 2000
#
#   Year 2000 projections >= 100 or < 0 are meaniningless        
#
    if (stdev < minsdev) and proj < 100 and proj > 0 :

        print('{:3d}\t{:5.3f}\t{:5.3f}\t{:s}'.format(m,stdev,proj,'viable'))
        ys= ??? # get y-coordinates of polynomial using x-coordinates in xData array
#
#       Use Matplotlib to plot original data points with validated curve fitting
#
        pylab.figure()
        pylab.xlabel("x")
        pylab.ylabel("Thermal Efficiency")
        my_title= 'Fit with poly degree = ' + str(m) + '; green dot is 2000 projection'
        pylab.title(my_title)
        pylab.xlim(???)            # x-axis values should range from 1710 to 2015
        pylab.plot(???)            # plot Year 2000 projection as a green dot
        pylab.plot(???)            # plot the original data given in the xData and yData
                                   # arrays as red dots
        pylab.plot(???)            # plot polynomial curve using xData and ys arrays
                                   # and make it blue.
        pylab.grid()
        fname='degree' + str(m) + 'fit.png' # save figure to file rather than display
        pylab.savefig(fname)
    else :
        print('{:3d}\t{:5.3f}\t{:5.3f}\t{:s}'.format(m,stdev,proj,'not viable'))
#--------------------------------------------------------------------------------------
# Table to stdout should look similar to this...
#
# Degree Stdev   2000P
#   1 	 2.855	 34.986	    viable
#   2	 2.768	 45.419	    viable
#   3	 2.266	 -6.602	    not viable
#   4	 2.234	 112.391.   not viable
#   5	 2.496	 113.726.   not viable
#--------------------------------------------------------------------------------------
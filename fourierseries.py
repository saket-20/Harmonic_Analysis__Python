# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sympy as sy

import numpy as np
from matplotlib import pyplot as plt

from sympy import fourier_series,pi,cos,sin

from sympy.abc import x,t

from sympy import Piecewise,And,plot

print("1:Fourier Series of a function in an interval")
print("2:Fourier Series of a piecewise function")#to be added
n=int(input("Enter your Choice"))
if n==1:
    expr1=input("Enter the function to find fourier series")

    expr1=sy.factor(expr1)
    try1=int(input("Enter 1 to enter interval in terms of pi or it's multiples,Otherwise enter 0"))
    if try1==1:
        interval1=int(input("Enter the multiple of pi that you want,Eg:2 represents 2*pi"))
        interval2=int(input("Enter the multiple of pi that you want,Eg:2 represents 2*pi"))
        interval1=interval1*pi
        interval2=interval2*pi
    else:
        interval1=float(input("Enter the Starting point of the interval"))
        interval2=float(input("Enter the Ending point of the interval"))

    
    s = fourier_series(expr1, (x,interval1,interval2 ))
    
    truncval=int(input("enter the number of terms desired in the fourier series"))

    v=s.truncate(truncval)

    print("FOURIER SERIES OF THE ENTERED FUNCTION\n\n\n")

    print(v)
    x1=[i for i in np.arange(interval1,interval2,0.02)]
    y1=[(v.evalf(subs={x:j})) for j in np.arange(interval1,interval2,0.02)]
    
    x2=[i for i in np.arange(interval1,interval2,0.0001)]
    y2=[(expr1.evalf(subs={x:j})) for j in np.arange(interval1,interval2,0.0001)]

    plt.plot(x1,y1,'red',label="GRAPH OF FOURIER SERIES")
    
    plt.plot(x2,y2,'green',label="ORIGINAL GRAPH OF THE FUNCTION")
    
    print("#PLOT IN GREEN SHOWS THE ACTUAL GRAPH OF THE FUNCTION")

    print("#PLOT IN RED SHOWS THE GRAPH OF THE FOURIER SERIES")
    plt.legend(loc="best")
    plt.title('Harmonic Analysis') 
    plt.show()
elif n==2:
    print("Enter all functions as functions of 't' ie. f(t)")
    fval1=input("Enter the Value of the piecewise function in the first interval")
    fval1=sy.factor(fval1)
    fval2=input("Enter the Value of the piecewise function in the second interval")
    fval2=sy.factor(fval2)
    try1=int(input("Enter 1 to enter limits in terms of pi,Else enter 0"))
    if try1==0:
        fval1_lowerlimit=float(input("Enter the lower limit for the first interval"))
        fval1_upperlimit=float(input("Enter the upper limit for the first interval"))
        fval2_lowerlimit=float(input("Enter the lower limit for the second interval"))
        fval2_upperlimit=float(input("Enter the upper limit for the second interval"))
    elif try1==1:
        fval1_lowerlimit=float(input("Enter the lower limit for the first interval in terms of multiples of pi,Eg:2 represents 2*pi"))
        fval1_upperlimit=float(input("Enter the upper limit for the first interval in terms of multiples of pi,Eg:2 represents 2*pi"))
        fval2_lowerlimit=float(input("Enter the lower limit for the second interval in terms of multiples of pi,Eg:2 represents 2*pi"))
        fval2_upperlimit=float(input("Enter the upper limit for the second interval in terms of multiples of pi,Eg:2 represents 2*pi"))
        fval1_lowerlimit=fval1_lowerlimit*pi
        fval1_upperlimit=fval1_upperlimit*pi
        fval2_lowerlimit=fval2_lowerlimit*pi
        fval2_upperlimit=fval2_upperlimit*pi
        
    
    truncval1=int(input("Enter the number of terms desired in the fourier series"))
    p=Piecewise((fval1,And(fval1_lowerlimit<t, t <fval1_upperlimit)),(fval2, And(t >fval2_lowerlimit,t<fval2_upperlimit)))
    fs = fourier_series(p, (t,fval1_lowerlimit,fval2_upperlimit)).truncate(truncval1)
    print("FOURIER SERIES OF THE ENTERED FUNCTION\n\n\n")
    print(fs)
    x1=[i for i in np.arange(fval1_lowerlimit,fval2_upperlimit,0.02)]
    y1=[(fs.evalf(subs={t:j})) for j in np.arange(fval1_lowerlimit,fval2_upperlimit,0.02)]
    
    x2=[i for i in np.arange(fval1_lowerlimit,fval2_upperlimit,0.0001)]
    y2=[(p.evalf(subs={t:j})) for j in np.arange(fval1_lowerlimit,fval2_upperlimit,0.0001)]

    plt.plot(x1,y1,'red',label="GRAPH OF FOURIER SERIES")
    plt.plot(x2,y2,'green',label="ORIGINAL GRAPH OF THE FUNCTION")
    
    print("\n\n#PLOT IN GREEN SHOWS THE ACTUAL GRAPH OF THE FUNCTION")

    print("\n\n#PLOT IN RED SHOWS THE GRAPH OF THE FOURIER SERIES")
    plt.legend(loc="best")
    
    plt.title('Harmonic Analysis')
    
    plt.show()


    



"""
File: smoothed_Heaviside.py

Copyright (c) 2016 Gabi Montes De Oca

License: MIT

<Defining a function>
"""

from math import pi, sin

def H_eps(x, eps=0.01):
    if x < -eps:
        result = 0
    elif x <= eps:
        x_over_eps = x/eps
        result = 0.5*(1.0+(x/eps)+(sin(pi* x_over_eps)/pi))
    else:
        result = 1
    return result


def test_H_eps():
    eps = 0.01
    if H_eps(-0.02) != 0:
        print "Error!"
    elif H_eps(-eps) != 0.5*(1.0+(x/eps)+(sin(pi* x_over_eps)/pi)):
        print "Error!"
    elif H_eps(0) != (1/2) + (x/(2*0)) + (1/(2*pi))*sin((pi*x)/0):
        print "Error!"
    elif H_eps(eps) != (1/2) + (x/(2*eps)) + (1/(2*pi))*sin((pi*x)/eps):
        print "Error!"
    elif H_eps(0.02) != 1:
        print "Error!"
    else:
        print "Good job!"

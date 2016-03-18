"""
File: Heaviside.py
Copyright (c) 2016 Gabi Montes De Oca
License: MIT
<Test a function for values>
"""

#a)
def H(x):
    if x < 0:
        return 0
    else:
        return  1

#b)
def test_H():
    if H(-10) != 0:
        print "Error"
    if H(-10**-15) != 0:
        print "Error"
    if H(0) != 1:
        print "Error"
    if H(10**-15) != 1:
        print "Error"
    if H(10)!= 1:
        print "Error"
    else:
        print "Good job!"

test_H()

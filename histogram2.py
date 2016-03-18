"""
File: histogram2.py
Copyright (c) Gabi Montes De Oca
License: MIT
<Enhanced histogram>
"""

ls= [4,9,13,5]

def histogram2(lst):
    print " n | Data"
    print "---+-------------------"

    for i in lst:
        st=""
        for j in range(i):
            st += "*"
        print len(st), "|", st

histogram2(ls)

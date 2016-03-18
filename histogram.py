"""
File: histogram.py
Copyright (c) 2016 Gabi Montes De Oca
License: MIT
<Making a histogram>
"""
ls=[4,9,13,5]
def histogram(n):
    st=""
    for i in range(n):
        st += "*"
    return st
for i in range(len(ls)):
    print histogram(ls[i])

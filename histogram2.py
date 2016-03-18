"""
File: histogram2.py
Copyright (c) Gabi Montes De Oca
License: MIT
<Enhanced histogram>
"""

user_input= raw_input("Enter a positive number here: ")
n=int(user_input)

def histogram2("Data", [4, 9, 13, 5]):
    print " n | Data"
    print "---+-------------------"
    st = ""
    for i in range(n):
        st = ""
        for j in range(n):
            st += "*"
print st "|" ls(4,9,13,5)

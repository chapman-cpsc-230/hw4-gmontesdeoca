"""
File: digits.py
Copyright (c) 2016 Gabi Montes De Oca
License: MIT
<Determining the number of digits in an integer>
"""

user_input=raw_input("Enter a number here: ")
n=int(user_input)

def digits(x):
    st=str(n)
    return len(st)
print digits(n)

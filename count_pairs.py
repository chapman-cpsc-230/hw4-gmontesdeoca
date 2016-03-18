"""
File: count_pairs.py
Copyright (c) 2016 Gabi Montes De Oca
License: MIT
<counting pairs in a string>
"""

def count_pairs (dna, pair):
    i=0
    dna=list(dna)
    for c in dna:
        if c == base:
            i +=1
    return 1
dna= 'ATGCGGACCTAT'
base= "AT"
n= count_pairs

print "%s appears %d times in %s" (base, n, dna)

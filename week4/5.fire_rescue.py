# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:57:06 2022

@author: nolan
"""

# n = 8
# m = [2, 7, 92, 1, 1, 2, 2, 92]
# for i in range():
#     pass


n=int(input())
a = [int(x) for x in input().split()]
   
def obf(lst):
    cnts = {}
    for e in lst:
        cnts[e] = cnts.get(e, 0) + 1
    return sorted(cnts, key=lambda e: (cnts[e], -e), reverse=True)
   
x=obf(a)
print('->'.join(str(xi) for xi in x))
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:33:22 2022

@author: nolan
"""

def get_array_numerd(b, t):
    g = []
    if t in b:
        for i in range(len(b)):
            if b[i] != t:
                g.append(b[i])

    else:
        g = b + [t]
   
    g.sort()
    return g

d = int(input())
a = list(map(int, input().split()))

t = int(input())


x = get_array_numerd(a, t)  # 1,2,4,5

print(*x)





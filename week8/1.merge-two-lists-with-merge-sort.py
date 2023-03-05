# -*- coding: utf-8 -*-
"""
Created on Sun May  1 15:22:05 2022

@author: nolan
"""

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []

for i in range(n+m):
    if len(a) == 0:
        c.append(b.pop(0))
    elif len(b) == 0:
        c.append(a.pop(0))
    else:
        if a[0] > b[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
print(*c)
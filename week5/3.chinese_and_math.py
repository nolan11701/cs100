# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:57:57 2022

@author: nolan
"""

n = int(input())
m = []
for blubber in range(n):
    m.append(list(map(int, input().split())))
for i in range(n-1):
    for j in range(n-1-i):
        if sum(m[j]) < sum(m[j+1]):
            m[j], m[j+1] = m[j+1], m[j]
        elif sum(m[j]) == sum(m[j+1]):
            if m[j][0] < m[j+1][0]:
                m[j], m[j+1] = m[j+1], m[j]
for lmnop in m:
    print(*lmnop, sep = "\n")
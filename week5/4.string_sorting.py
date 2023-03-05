# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:14:20 2022

@author: nolan
"""

n = int(input())
m = []
for b in range(n):
    m.append(input())

for i in range(n-1):
    for j in range(n-1-i):
        if m[j] > m[j+1]:
            m[j], m[j+1] = m[j+1], m[j]
print(*m, sep = "\n")
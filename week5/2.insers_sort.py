# Insertion sort in Python

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 19:00:43 2022

@author: nolan
"""

n = int(input())
m = list(map(int, input().split()))
 
for i in range(1, n):
    c = m[i]
 
    for j in range(i, -1, -1):
     
        if c < m[j-1] and j>0:
            m[j] = m[j-1]
        else:
            m[j] = c
            break
 
print(*m)
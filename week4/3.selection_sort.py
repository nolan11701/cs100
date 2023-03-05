# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:01:02 2022

@author: nolan
"""

# n = 5

# m = [1, 4, 2, 3, 5]

n = int(input())
m = list(map(int,input().split()))

for i in range(n-1):
    pos = i
    for j in range(i+1, n):
        if m[j] < m[pos]:
            pos = j
    m[i], m[pos] = m[pos], m[i]
    
print(*m)
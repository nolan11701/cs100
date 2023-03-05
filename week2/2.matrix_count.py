# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:41:49 2022

@author: nolan
"""
# n, m = 3, 5
# matrix = [
# [0,0,1,1,0],
# [0,1,1,0,1],
# [1,0,0,1,0]
# ]

n,m = map(int, input().split())
matrix = []

for f in range(n):
    matrix.append(list(map(int, input().split())))
    
b = [0]*m

for i in range(m):
    for j in range(n):
        b[i] += matrix[j][i]

print(*b, sep = "\n")
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:55:40 2022

@author: nolan
"""

# n, m = 5, 4
# matrix = [
# [3,3,3,4],
# [2,0,0,3],
# [0,3,1,4],
# [3,4,3,3],
# [1,0,3,3]
# ]

n,m = map(int, input().split())
matrix = []
for f in range(n):
    matrix.append(list(map(int, input().split())))
b = []
for i in range(m):
    for j in range(n-1, -1, -1):
        b.append((matrix[j][i]))
z = [[0 for i in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        z[i][j] = b[i*n+j]
for i in range(len(z)):
    z[i].reverse()
    print(*z[i])
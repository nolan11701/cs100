# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 18:45:47 2022

@author: nolan
"""

    # matrix = [
    # [-34,95,-85,26,-57],
    # [8,33,-36,69,-4],
    # [-36,-55,-92,96,-70],
    # [79, -93, -42, -44, 66]
    # ]
    
n,m = map(int, input().split())
matrix = []

for b in range(n):
    matrix.append(list(map(int, input().split())))

k = [[0 for x in range(n)] for y in range(m)]
for i in range(n):
    for j in range(m):
        k[i][j] = abs(matrix[i][j])
        
for lst in k:
    print(*lst, sep = " ")

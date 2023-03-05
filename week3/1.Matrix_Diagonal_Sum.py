# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:22:22 2022

@author: nolan
"""
# n = 3
# m = [[1,2,3], [4,5,6], [7,8,9]]
# HELLO

n = int(input())
matrix = []
for f in range(n):
    matrix.append(list(map(int, input().split())))

s = 0

for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            s+=matrix[i][j]
print(s)
        
    
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:11:02 2022

@author: nolan
"""

# n = 2
# A = [[3,4],[2,1]]
# B = [[1,5],[3,7]]

n = int(input())
A, B = [], []
for a in range(n):
    A.append(list(map(int, input().split()))) 
for b in range(n):
    B.append(list(map(int, input().split())))    


m = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            #print("m["+str(i)+"]["+str(j)+"] = A["+str(i)
            #      +"]["+str(k)+"] * B["+str(k)+"]["+str(j)+"]")
            m[i][j] += A[i][k] * B[k][j]
for ha in m:
    print(*ha)
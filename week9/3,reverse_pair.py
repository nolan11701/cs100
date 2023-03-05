# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:39:11 2022

@author: nolan
"""

n = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(n):
        if i<j and A[i] > A[j]:
            count += 1
print(count)
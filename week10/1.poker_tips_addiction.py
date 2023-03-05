# -*- coding: utf-8 -*-
"""
Created on Sun May  8 18:40:36 2022

@author: nolan
"""

def bubble_sort_with_two(m, b):
    n = len(m)
    for i in range(n-1):
        for j in range(n-1-i):
            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]
                b[j], b[j+1] = b[j+1], b[j]
    return m

n = int(input())
m = list(map(int, input().split()))
a = []
b = []

for i in range(n):
    if m[i] not in a:
        a.append(m[i])
        b.append(1)
    elif m[i] in a:
        b[a.index(m[i])]+=1
        
bubble_sort_with_two(a, b)

for j in range(len(a)):
    print(a[j], b[j], end="\n")

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:08:26 2022

@author: nolan
"""

# n = int(input())
# m = list(map(int, input().split()))
n = 10
m = [10, 9, 8, 7, 6, 5 ,4 ,3 ,2,1]
# bubble sort 

count = 0

for i in range(n-1):
    for j in range(n-1-i):
        if m[j] > m[j+1]:
            m[j], m[j+1] = m[j+1], m[j]
        count += 1
            
print(*m)

print(count)
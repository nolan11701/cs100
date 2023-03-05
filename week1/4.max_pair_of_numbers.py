# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 11:55:36 2022

@author: nolan
"""

# n, m = map(int, input().split())
# n1 = list(map(int, input().split()))
# m1 = list(map(int, input().split()))

# print(max(n1)+ max(m1))

l = [1,2,3,4,5,6,7,1,2,3,3,5,15,1,9]
index = 0
# find the index of the max item

for i in range(len(l)):
    if l[i] < l[index]:
        index = i
    
print(index, l[index])
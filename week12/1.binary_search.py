# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:20:25 2022

@author: nolan
"""

# n = 7
# f = 4
# m = [1,2,4,4,5,7,9]

n, f = map(int, input().split())
m = list(map(int, input().split()))

def binary_search(lst, f):
    l = 0
    r = len(lst)-1
    while l<=r:
        mid = (l+r)//2
        if lst[mid] < f:
            l = mid+1
        elif lst[mid] > f:
            r = mid-1
        else: 
            return mid
    return -1

print(binary_search(m, f)+1)
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:35:25 2022

@author: nolan
"""

# n = 7
# f = 4
# m = [1,2,4,4,5,7,9]

n, f = map(int, input().split())
lst = list(map(int, input().split()))

l = 0
r = len(lst)-1
result = 0

while l<=r:
    mid = (l+r)//2
    if lst[mid] < f:
        l = mid+1
    elif lst[mid] > f:
        r = mid-1
    else: 
        result = lst[mid]
        
print(result, mid,l,r)
if result != mid:
    l, r = r, l
    if lst[r]-f >= f-lst[l]:
        result = lst[l]
    else:
        result = lst[r]
        
print(result)
